from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from icecream import ic  # noqa: F401

import numpy as np
import utils.debug  # noqa: F401

from utils.harmonic import (
    get_harmonic_oscillation,
    get_period,
    get_phase_at
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
    """
    `Сложение гармонических колебаний колебания c различными фазами.`
    """
    fs = 1000
    A = 2
    f = 3

    func_vals = []
    t = get_linspace(start=0, stop=3 * get_period(f), fs=fs)

    func_vals.append(
        get_harmonic_oscillation(A, f, np.pi / 4, wave=np.cos)(t)
    )
    func_vals.append(
        get_harmonic_oscillation(A, f, np.pi / 3, wave=np.cos)(t)
    )

    x_sum = sum(func_vals)
    A_result = x_sum.max()
    phi_result = -get_phase_at(f, t[x_sum.argmax()]) % (2 * np.pi)

    ic(A_result, phi_result)

    show_plot(
        t=t,
        func_val=x_sum,
        title="сумма двух гармонических колебаний с одинаковой частотой"
    )

    func_vals.append(
        get_harmonic_oscillation(A, f, -np.pi / 6, wave=np.cos)(t)
    )

    x_sum = sum(func_vals)
    A_result = x_sum.max()
    phi_result = -get_phase_at(f, t[x_sum.argmax()]) % (2 * np.pi)

    ic(A_result, phi_result)

    show_plot(
        t=t,
        func_val=x_sum,
        title="сумма трёх гармонических колебаний с одинаковой частотой"
    )


def task_4() -> None:
    """
    `Сложение гармонических колебаний колебания c различными частотами и
    начальными фазами.`
    """
    fs = 2000
    f = 5

    func_vals = []
    t = get_linspace(start=0, stop=5 * get_period(f), fs=fs)

    func_vals.append(
        get_harmonic_oscillation(4 / np.pi, f, -np.pi / 2, wave=np.cos)(t)
    )
    func_vals.append(
        get_harmonic_oscillation(4 / (3 * np.pi), 3 * f, -np.pi / 2, wave=np.cos)(t)
    )

    show_plot(
        t=t,
        func_val=sum(func_vals),
        title="x(t) = 4/pi*cos(2*pi*f*t-pi/2) + 4/3*pi*cos(2*pi*3*f*t-pi/2)"
    )

    func_vals = []
    labels = []

    for n in range(0, 6, 2):
        func_vals.append(
            get_harmonic_oscillation(
                4 / ((2 * n - 1) * np.pi), (2 * n - 1) * f, -np.pi / 2, wave=np.cos
            )(t)
        )
        labels.append(f"N = {n + 1}")

    show_multi_plot(
        t=t,
        func_vals=[sum(func_vals[:i + 1]) for i in range(len(func_vals))],
        labels=labels,
        title="сумма колебаний по формуле"
    )


def main() -> None:
    task_1()
    task_2()

    print("-" * 50)
    task_3()
    print("-" * 50)

    task_4()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
