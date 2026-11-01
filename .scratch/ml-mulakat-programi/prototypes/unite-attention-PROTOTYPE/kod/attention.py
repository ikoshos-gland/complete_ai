"""PROTOTYPE - Ünite: Attention · Sıfırdan kod görevi (Implement).

Görev: aşağıdaki iki fonksiyonu yalnızca NumPy ile yaz.
Testler: `uv run pytest kod/` (bu klasörde).
Kural: torch / scipy yok. Döngü yalnızca head sayısı üzerinde serbest; T üzerinde döngü kurma.
"""
import numpy as np


def softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    """Sayısal olarak kararlı softmax. -inf girdileri 0 olasılık almalı."""
    raise NotImplementedError


def scaled_dot_product_attention(
    q: np.ndarray,  # (..., T_q, d_k)
    k: np.ndarray,  # (..., T_k, d_k)
    v: np.ndarray,  # (..., T_k, d_v)
    causal: bool = False,
) -> tuple[np.ndarray, np.ndarray]:
    """(output, weights) döndür. output: (..., T_q, d_v), weights: (..., T_q, T_k).

    causal=True ise i. sorgu yalnızca j <= i anahtarlarına bakabilir.
    """
    raise NotImplementedError


def multi_head_attention(
    x: np.ndarray,  # (B, T, d_model)
    w_q: np.ndarray,  # (d_model, d_model)
    w_k: np.ndarray,
    w_v: np.ndarray,
    w_o: np.ndarray,
    n_heads: int,
    causal: bool = True,
) -> np.ndarray:
    """(B, T, d_model) döndür. d_head = d_model // n_heads."""
    raise NotImplementedError
