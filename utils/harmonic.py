from typing import Callable
import numpy as np


def get_harmonic_oscillation(
    a: float,
    f: float,
    phi: float,
    wave: Callable[[np.ndarray], np.ndarray] = np.sin
) -> Callable[[np.ndarray], np.ndarray]:
    """y = a * wave(2 * pi * f * t + phi)"""
    def y(t: np.ndarray) -> np.ndarray:
        return a * wave(2 * np.pi * f * t + phi)

    return y


def get_period(f: float) -> float:
    """T = 1/f"""
    return 1 / f


def get_phase_time_shift(phi: float, f: float) -> float:
    """-phi / (2 * pi * f)"""
    # угол делится на 2*pi, чтобы получить долю периода, затем умножается на период (делится на фазу)
    return -phi / (2 * np.pi * f)


def get_phase_at(f: float, t: np.ndarray, phi: float = 0) -> np.ndarray:
    """(2 * pi * f * t) + phi"""
    # время умножается на частоту и на 2*pi, чтобы получить фазу в радианах + начальная фаза
    return 2 * np.pi * f * t + phi
