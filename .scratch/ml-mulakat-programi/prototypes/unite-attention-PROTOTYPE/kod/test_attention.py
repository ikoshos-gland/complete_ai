"""PROTOTYPE - Implement görevinin testleri. Hepsi geçince görev biter."""
import os
import importlib

import numpy as np
import pytest

# ATTN_IMPL=cozumler.attention_cozum ile referans çözüme karşı da koşturulabilir.
attn = importlib.import_module(os.environ.get("ATTN_IMPL", "kod.attention"))

rng = np.random.default_rng(0)


def naive_attention(q, k, v, causal):
    """Satır satır, döngülü referans. Yavaş ama apaçık doğru."""
    T_q, d_k = q.shape
    out = np.zeros((T_q, v.shape[-1]))
    for i in range(T_q):
        scores = np.array([q[i] @ k[j] / np.sqrt(d_k) for j in range(k.shape[0])])
        if causal:
            scores[i + 1 :] = -np.inf
        w = np.exp(scores - scores.max())
        w /= w.sum()
        out[i] = w @ v
    return out


def test_softmax_rows_sum_to_one():
    p = attn.softmax(rng.normal(size=(4, 7)))
    np.testing.assert_allclose(p.sum(-1), 1.0, atol=1e-12)


def test_softmax_is_stable_for_large_logits():
    p = attn.softmax(np.array([[1000.0, 1001.0, 1002.0]]))
    assert np.isfinite(p).all()
    np.testing.assert_allclose(p, attn.softmax(np.array([[0.0, 1.0, 2.0]])))


def test_softmax_handles_neg_inf():
    p = attn.softmax(np.array([[0.0, -np.inf, 0.0]]))
    np.testing.assert_allclose(p, [[0.5, 0.0, 0.5]])


@pytest.mark.parametrize("causal", [False, True])
def test_sdpa_matches_naive_loop(causal):
    q, k, v = rng.normal(size=(6, 8)), rng.normal(size=(6, 8)), rng.normal(size=(6, 5))
    out, w = attn.scaled_dot_product_attention(q, k, v, causal=causal)
    assert out.shape == (6, 5) and w.shape == (6, 6)
    np.testing.assert_allclose(out, naive_attention(q, k, v, causal), atol=1e-10)


def test_sdpa_batched_leading_dims():
    q = rng.normal(size=(2, 3, 4, 8))
    out, w = attn.scaled_dot_product_attention(q, q, q)
    assert out.shape == (2, 3, 4, 8) and w.shape == (2, 3, 4, 4)


def test_causal_weights_are_lower_triangular():
    q = rng.normal(size=(5, 4))
    _, w = attn.scaled_dot_product_attention(q, q, q, causal=True)
    assert np.allclose(np.triu(w, k=1), 0.0)


def _mha_params(d_model):
    return [rng.normal(size=(d_model, d_model)) / np.sqrt(d_model) for _ in range(4)]


def test_mha_shape():
    x = rng.normal(size=(2, 5, 16))
    out = attn.multi_head_attention(x, *_mha_params(16), n_heads=4)
    assert out.shape == (2, 5, 16)


def test_mha_causal_no_future_leak():
    """t. pozisyonun çıktısı t'den sonraki token'lar değişince değişmemeli."""
    x = rng.normal(size=(1, 6, 16))
    params = _mha_params(16)
    out1 = attn.multi_head_attention(x, *params, n_heads=4, causal=True)
    x2 = x.copy()
    x2[:, 4:] = rng.normal(size=(1, 2, 16))
    out2 = attn.multi_head_attention(x2, *params, n_heads=4, causal=True)
    np.testing.assert_allclose(out1[:, :4], out2[:, :4], atol=1e-10)


def test_mha_one_head_equals_sdpa():
    """n_heads=1 iken MHA = projeksiyon + SDPA + çıkış projeksiyonu."""
    x = rng.normal(size=(1, 5, 8))
    wq, wk, wv, wo = _mha_params(8)
    out = attn.multi_head_attention(x, wq, wk, wv, wo, n_heads=1, causal=True)
    ref = naive_attention(x[0] @ wq, x[0] @ wk, x[0] @ wv, causal=True) @ wo
    np.testing.assert_allclose(out[0], ref, atol=1e-10)


def test_mha_heads_are_independent():
    """Sadece 0. head'in Q ağırlıkları değişirse, diğer head'lerin katkısı aynı kalmalı.
    Yanlış reshape (transpose'suz) head'leri birbirine karıştırır ve bu testi düşürür."""
    d, H = 16, 4
    dh = d // H
    x = rng.normal(size=(1, 5, d))
    wq, wk, wv, wo = _mha_params(d)
    wo_masked = wo.copy()
    wo_masked[:dh] = 0.0  # 0. head'in çıkışını sıfırla
    a = attn.multi_head_attention(x, wq, wk, wv, wo_masked, n_heads=H)
    wq2 = wq.copy()
    wq2[:, :dh] = rng.normal(size=(d, dh))  # yalnızca 0. head'in sorgusunu boz
    b = attn.multi_head_attention(x, wq2, wk, wv, wo_masked, n_heads=H)
    np.testing.assert_allclose(a, b, atol=1e-10)
