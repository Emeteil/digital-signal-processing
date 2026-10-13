from typing import Callable, Sequence
import numpy as np

from utils.fourier import integrate


def get_convolution_product(
    s1: Callable[[np.ndarray], np.ndarray],
    s2: Callable[[np.ndarray], np.ndarray],
    tau: np.ndarray,
    t: float
) -> np.ndarray:
    """s2(τ)s1(t - τ)"""
    return s2(tau) * s1(t - tau)


def get_convolution(
    s1: Callable[[np.ndarray], np.ndarray],
    s2: Callable[[np.ndarray], np.ndarray],
    tau: np.ndarray,
    t: float
) -> float:
    """∫s2(τ)s1(t - τ)dτ"""
    return integrate(get_convolution_product(s1, s2, tau, t), tau)


def get_convolution_series(
    s1: Callable[[np.ndarray], np.ndarray],
    s2: Callable[[np.ndarray], np.ndarray],
    tau: np.ndarray,
    t: Sequence[float]
) -> np.ndarray:
    """значения интеграла свертки для набора моментов времени t"""
    return np.array([get_convolution(s1, s2, tau, ti) for ti in t])
