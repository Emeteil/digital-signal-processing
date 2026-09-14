from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from icecream import ic  # noqa: F401

import utils.debug  # noqa: F401

from utils.plotting import show_plot
from utils.sampling import build_digital_signal_samples


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

    t, func_val = build_digital_signal_samples(
        digital_signal=digital_signal,
        start=start,
        stop=stop,
        fs=fs
    )

    ic(digital_signal)

    show_plot(
        t=t,
        func_val=func_val,
        is_stem=False,
        is_enable_ion=False
    )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
