import numpy as np


def to_polar(z: complex) -> tuple[float, float]:
    """to_polar(z) -> r, theta"""
    # abs - теорема Пифагора, angle - арктангенс
    return np.abs(z), np.angle(z)


def to_rect(r: float, theta: float) -> complex:
    """to_rect(r, theta) -> z"""
    # просто формула Эйлера из тфкп
    return r * (np.cos(theta) + 1j * np.sin(theta))
