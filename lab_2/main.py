from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from icecream import ic  # noqa: F401

import numpy as np
import utils.debug  # noqa: F401

from utils.harmonic import (
    get_harmonic_oscillation,
    get_period
)
from utils.plotting import show_multi_plot, show_plot
from utils.sampling import get_linspace


def task_1() -> None:
    """
    `Выполните моделирование колебаний с различной амплитудой, частотой и
    длительностью.`
    """
    fs = 1000
    phi = 0

    func_vals = []
    labels = []
    t = []

    labels.append("A = 5, f = 3, stop = 2")
    t.append(get_linspace(start=0, stop=2, fs=fs))
    func_vals.append(
        get_harmonic_oscillation(5, 3, phi)(t[-1])
    )

    labels.append("A = 4, f = 4, stop = 3")
    t.append(get_linspace(start=0, stop=3, fs=fs))
    func_vals.append(
        get_harmonic_oscillation(4, 4, phi)(t[-1])
    )

    labels.append("A = 2, f = 0.7, stop = 5")
    t.append(get_linspace(start=0, stop=5, fs=fs))
    func_vals.append(
        get_harmonic_oscillation(2, 0.7, phi)(t[-1])
    )

    labels.append("A = 8, f = 1, stop = 4.6")
    t.append(get_linspace(start=0, stop=4.6, fs=fs))
    func_vals.append(
        get_harmonic_oscillation(8, 1, phi)(t[-1])
    )

    show_multi_plot(
        t=t,
        func_vals=func_vals,
        labels=labels,
        title="гармоническое колебание с различными A, f, stop"
    )


def task_2() -> None:
    """
    `Выполните моделирование колебаний с различными начальными фазами.`
    """
    fs = 1000
    A = 5
    f = 3

    func_vals = []
    labels = []
    t = get_linspace(start=0, stop=3 * get_period(f), fs=fs)

    labels.append("ф = pi / 2")
    func_vals.append(
        get_harmonic_oscillation(A, f, np.pi / 2)(t)
    )

    labels.append("ф = -pi / 3")
    func_vals.append(
        get_harmonic_oscillation(A, f, -np.pi / 3)(t)
    )

    labels.append("ф = pi / 4")
    func_vals.append(
        get_harmonic_oscillation(A, f, np.pi / 4)(t)
    )

    labels.append("ф = pi / 5")
    func_vals.append(
        get_harmonic_oscillation(A, f, np.pi / 5)(t)
    )

    show_multi_plot(
        t=t,
        func_vals=func_vals,
        labels=labels,
        title="гармоническое колебание с различными A, f, stop"
    )


def task_3() -> None:
    # """
    # `Выполните моделирование колебаний с различными начальными фазами.`
    # """
    fs = 1000
    A = 2

    func_vals = []
    t = get_linspace(start=0, stop=3, fs=fs)

    func_vals.append(
        get_harmonic_oscillation(A, 3, np.pi / 2)(t)
    )

    func_vals.append(
        get_harmonic_oscillation(A, 2, -np.pi / 3)(t)
    )

    show_plot(
        t=t,
        func_val=sum(func_vals),
        title="гармоническое колебание с различными A, f, stop"
    )

    func_vals = []

    func_vals.append(
        get_harmonic_oscillation(A, 3, np.pi / 4)(t)
    )

    func_vals.append(
        get_harmonic_oscillation(A, 2, np.pi / 5)(t)
    )

    func_vals.append(
        get_harmonic_oscillation(A, 20, np.pi / 2)(t)
    )

    show_plot(
        t=t,
        func_val=sum(func_vals),
        title="гармоническое колебание с различными A, f, stop"
    )


def main() -> None:
    task_1()
    task_2()
    task_3()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
