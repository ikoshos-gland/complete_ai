"""PROTOTYPE - Referans çözüm. Öğrenen görevi bitirmeden açmaz."""
import numpy as np


def softmax(x, axis=-1):
    m = np.max(x, axis=axis, keepdims=True)
    m = np.where(np.isfinite(m), m, 0.0)
    e = np.exp(x - m)
    return e / e.sum(axis=axis, keepdims=True)


def scaled_dot_product_attention(q, k, v, causal=False):
    d_k = q.shape[-1]
    scores = q @ np.swapaxes(k, -1, -2) / np.sqrt(d_k)
    if causal:
        T_q, T_k = scores.shape[-2:]
        mask = np.triu(np.ones((T_q, T_k), dtype=bool), k=1)
        scores = np.where(mask, -np.inf, scores)
    w = softmax(scores, axis=-1)
    return w @ v, w


def multi_head_attention(x, w_q, w_k, w_v, w_o, n_heads, causal=True):
    B, T, d = x.shape
    dh = d // n_heads

    def split(t):  # (B,T,d) -> (B,H,T,dh)
        return t.reshape(B, T, n_heads, dh).transpose(0, 2, 1, 3)

    q, k, v = split(x @ w_q), split(x @ w_k), split(x @ w_v)
    out, _ = scaled_dot_product_attention(q, k, v, causal=causal)
    out = out.transpose(0, 2, 1, 3).reshape(B, T, d)
    return out @ w_o
