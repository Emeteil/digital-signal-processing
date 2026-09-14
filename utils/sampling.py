from typing import Sequence
import numpy as np


def get_linspace(
    start: float = 0,
    stop: float = 1,
    fs: float = 100,
    is_arange: bool = False
) -> np.ndarray:
    ts = (stop - start) / fs

    if is_arange:
        t = np.arange(start, stop, ts)
    else:
        t = np.linspace(start, stop, fs, endpoint=False)

    return t


def build_digital_signal_samples(
    digital_signal: Sequence[int],
    start: float,
    stop: float,
    fs: float
) -> tuple[list[float], list[int]]:
    samples_per_bit = int(((stop - start) * fs) / len(digital_signal))
    func_val = [x for x in digital_signal for _ in range(samples_per_bit)]
    t = [start + i / fs for i in range(len(func_val))]
    return t, func_val
