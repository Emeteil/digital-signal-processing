from typing import Callable
import numpy as np


def discrete_fourier_transform(x: np.ndarray) -> np.ndarray:
    N = len(x)
    X = []
    for k in range(N):
        s = 0
        for n in range(N):
            s += x[n] * np.exp(-2j * np.pi * k * n / N)
        X.append(s)
    
    return np.array(X)

    
def _get_a_b(n: int, x_t: np.ndarray, t: np.ndarray, f: float, wave: Callable[[float], float]) -> float:
    T = 1 / f
    Ts = t[1] - t[0]
    m = x_t * wave(2 * np.pi * n * f * t)
    return 2 / T * np.sum(m) * Ts
    

def get_a(n: int, x_t: np.ndarray, t: np.ndarray, f: float) -> float:
    return _get_a_b(n, x_t, t, f, np.cos)
    
def get_b(n: int, x_t: np.ndarray, t: np.ndarray, f: float) -> float:
    return _get_a_b(n, x_t, t, f, np.sin)