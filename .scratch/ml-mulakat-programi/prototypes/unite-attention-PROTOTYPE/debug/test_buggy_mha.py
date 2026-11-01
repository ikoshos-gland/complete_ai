"""PROTOTYPE - Debug görevinin testleri. Referans: cozumler/attention_cozum.py."""
import numpy as np

from debug import buggy_mha as bug
from cozumler import attention_cozum as ref

rng = np.random.default_rng(1)


def _params(d):
    return [rng.normal(size=(d, d)) / np.sqrt(d) for _ in range(4)]


def test_matches_reference():
    x = rng.normal(size=(2, 6, 16))
    p = _params(16)
    np.testing.assert_allclose(
        bug.multi_head_attention(x, *p, n_heads=4),
        ref.multi_head_attention(x, *p, n_heads=4),
        atol=1e-10,
    )


def test_causal_rows_are_distributions():
    """Maskeden sonra her sorgunun ağırlıkları hâlâ 1'e toplanmalı.
    V = birim vektörler verilirse çıktı satır toplamı ağırlık toplamına eşittir."""
    T = 5
    x = rng.normal(size=(1, T, 4))
    eye = np.eye(4)
    out = bug.multi_head_attention(x, eye, eye, np.ones((4, 4)) / 4, eye, n_heads=1)
    # V'nin her satırı x'in ortalaması -> çıktı = (ağırlık toplamı) * ortalama
    expected = ref.multi_head_attention(x, eye, eye, np.ones((4, 4)) / 4, eye, n_heads=1)
    np.testing.assert_allclose(out, expected, atol=1e-10)


def test_no_nan_with_large_activations():
    x = rng.normal(size=(1, 8, 16)) * 60.0
    out = bug.multi_head_attention(x, *_params(16), n_heads=4)
    assert np.isfinite(out).all()
