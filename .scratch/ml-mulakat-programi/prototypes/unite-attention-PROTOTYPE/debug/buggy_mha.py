"""PROTOTYPE - Ünite: Attention · Debug görevi.

Senaryo: Bir arkadaşın küçük bir GPT eğitiyor. Loss ilk yüz adımda güzelce düşüyor,
ama doğrulama setindeki üretimler anlamsız ve uzun dizilerde loss bir anda NaN oluyor.
Kodda 3 hata var. Her birini bul, düzelt ve neden bu belirtiye yol açtığını
bir cümleyle İngilizce yaz (mülakatta söyleyeceğin cümle).

Testler: `uv run pytest debug/`. Başta 3 test düşmeli.
İpucu bütçesi: Hoca'dan en fazla 1 ipucu iste.
"""
import numpy as np


def softmax(x, axis=-1):
    e = np.exp(x)
    return e / e.sum(axis=axis, keepdims=True)


def multi_head_attention(x, w_q, w_k, w_v, w_o, n_heads, causal=True):
    B, T, d = x.shape
    dh = d // n_heads

    def split(t):
        return t.reshape(B, n_heads, T, dh)

    q, k, v = split(x @ w_q), split(x @ w_k), split(x @ w_v)
    scores = q @ k.transpose(0, 1, 3, 2) / np.sqrt(dh)
    w = softmax(scores)
    if causal:
        w = w * np.tril(np.ones((T, T)))
    out = (w @ v).transpose(0, 2, 1, 3).reshape(B, T, d)
    return out @ w_o
