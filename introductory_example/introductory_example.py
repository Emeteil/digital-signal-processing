import numpy as np
import matplotlib.pyplot as plt
from typing import Callable
from icecream import ic

is_enable_ic = True


def get_harmonic_oscillation(
    a: float, f: float, phi: float
) -> Callable[[float], float]:
    def y(t: float) -> float:
        return a * np.sin(2 * np.pi * f * t + phi)

    return y


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


def show_plot(
    t: np.ndarray,
    func_val: np.ndarray,
    is_stem: bool = False,
    is_enable_ion: bool = False
) -> None:
    if is_enable_ion:
        plt.ion()

    if not is_enable_ic:
        ic.disable()

    if is_stem:
        plt.stem(t, func_val)
    else:
        plt.plot(t, func_val)

    plt.grid()

    try:
        plt.show()
    except KeyboardInterrupt:
        pass


def main() -> None:
    start = 0
    stop = 1
    fs = 1000

    # a = 1
    # f = 10
    # phi = 0

    # t = get_linspace(
    #      start=start,
    #     stop=stop,
    #     fs=fs
    # )

    # y_1 = get_harmonic_oscillation(a=a, f=f, phi=phi)

    # func_val = y_1(t) + np.random.normal(0, 0.3, fs)

    digital_signal = [0, 0, 0, 1, 1, 0, 1]

    samples_per_bit = int(((stop - start) * fs) / len(digital_signal))
    func_val = [x for x in digital_signal for _ in range(samples_per_bit)]
    t = [start + i / fs for i in range(len(func_val))]

    show_plot(
        t=t,
        func_val=func_val,
        is_stem=False,
        is_enable_ion=False
    )


if __name__ == "__main__":
    main()
