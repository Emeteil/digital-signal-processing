from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from icecream import ic  # noqa: F401

import numpy as np
import utils.debug  # noqa: F401
from matplotlib.axes import Axes

from utils.complex_numbers import to_polar, to_rect
from utils.harmonic import (
    get_harmonic_oscillation,
    get_period,
    get_phase_time_shift,
    get_phase_at,
)
from utils.plotting import show_multi_plot
from utils.sampling import get_linspace


def task_1() -> None:
    """
    `Найдите период и временной сдвиг максимума, соответствующий фазовому
    сдвигу. Изобразите сигнал с выбранными параметрами на интервале 2-3 периодов
    колебания. Для сравнения изобразите сигнал с нулевой начальной фазой.`
    """
    fs = 1000

    a = 4
    f0 = 0.2  # 0.4 / 2
    phi = 0.25 * np.pi  # 0.785398

    period = get_period(f0)
    t_max_shift = get_phase_time_shift(phi, f0)

    ic(a, f0, phi, period, t_max_shift)

    n_periods = 3
    t = get_linspace(start=0, stop=n_periods * period, fs=fs)

    y_phi = get_harmonic_oscillation(a, f0, phi, wave=np.cos)(t)
    y_zero_phi = get_harmonic_oscillation(a, f0, 0, wave=np.cos)(t)

    def mark_max_shift(ax: Axes) -> None:
        ax.axvline(
            t_max_shift + period,  # + период чтобы увидеть линию
            linestyle="--",
            label=f"t_max_shift={t_max_shift:.3f} с"
        )

    show_multi_plot(
        t=t,
        func_vals=[y_phi, y_zero_phi],
        labels=[f"φ={phi:.3f}.. радиан", "φ=0 радиан"],
        title="гармоническое колебание с начальной фазой и без",
        on_axes=mark_max_shift
    )


def task_2() -> None:
    """
    `Выберите значение периода колебания (2-10 секунд) и для сигнала
    с нулевой начальной фазой вычислите значение фазы колебания в
    моменты времени -1, 3, 7 сек`
    """
    period = 5
    f0 = 1 / period  # 0.2
    moments = [-1, 3, 7]

    for t in moments:
        discription = "Фаза для:"
        phase = get_phase_at(f0, t, phi=0)
        ic(discription, t, f0, period, phase)


def task_3() -> None:
    """
    `Для комплексных чисел z1 = a + jb и z2 = a − jb выберите значения a и
    b, найдите представление чисел в полярной форме.`
    """
    a = 3
    b = 4

    z1 = complex(a, b)
    z2 = complex(a, -b)

    r1, theta1 = to_polar(z1)
    r2, theta2 = to_polar(z2)

    discription_z1 = "Комплексное число z1 в полярной форме:"
    discription_z2 = "Комплексное число z2 в полярной форме:"

    ic(discription_z1, z1, r1, theta1)
    ic(discription_z2, z2, r2, theta2)


def task_4() -> None:
    """
    `Задайте комплексное число в полярной форме и преобразуйте его в обычную форму`
    """
    r = 5
    theta = np.pi / 3  # 1.04719

    z = to_rect(r, theta)

    discription = "Комплексное число в обычной форме:"
    ic(discription, r, theta, z)


def main() -> None:
    task_1()
    print("-" * 50)
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
