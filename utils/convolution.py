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


def get_rect_convolution_limits(
    width_1: float,
    width_2: float,
    t: float
) -> tuple[float, float]:
    """пределы интегрирования для двух прямоугольных импульсов с центром в нуле: [max(-w2/2, t - w1/2), min(w2/2, t + w1/2)]"""
    lower = max(-width_2 / 2, t - width_1 / 2)
    upper = min(width_2 / 2, t + width_1 / 2)
    return lower, upper


def get_rect_convolution_analytic(
    a_1: float,
    width_1: float,
    a_2: float,
    width_2: float,
    t: float
) -> float:
    """∫s2(τ)s1(t - τ)dτ = a1 * a2 * (верхний предел - нижний предел), если пределы пересекаются, иначе 0"""
    lower, upper = get_rect_convolution_limits(width_1, width_2, t)
    return a_1 * a_2 * max(0.0, upper - lower)


def get_convolution_series(
    s1: Callable[[np.ndarray], np.ndarray],
    s2: Callable[[np.ndarray], np.ndarray],
    tau: np.ndarray,
    t: Sequence[float]
) -> np.ndarray:
    """значения интеграла свертки для набора моментов времени t"""
    return np.array([get_convolution(s1, s2, tau, ti) for ti in t])
