from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from icecream import ic  # noqa: F401

import numpy as np
import utils.debug  # noqa: F401

from utils.harmonic import (
    get_harmonic_oscillation,
    get_single_rect_oscillation,
)
from utils.plotting import show_subplots
from utils.sampling import get_linspace
from utils.fourier import get_fourier_transform

FS = 4000
T_WINDOW = 20
EPS = 1e-2


def _get_spectrum(x_t: np.ndarray, t: np.ndarray, f: np.ndarray) -> np.ndarray:
    return np.array([get_fourier_transform(x_t, t, fi) for fi in f])


def _get_phase(X: np.ndarray) -> np.ndarray:
    phase = np.angle(np.where(np.abs(X.imag) < EPS, X.real, X))
    phase[np.abs(X) < EPS] = np.nan
    return phase


def _get_time_axis() -> np.ndarray:
    return get_linspace(start=-T_WINDOW / 2, stop=T_WINDOW / 2, fs=FS)


def _draw_spectra(
    f_list: list[np.ndarray],
    X_list: list[np.ndarray],
    labels: list[str],
    ticks: np.ndarray,
) -> None:
    def draw_mod(ax):
        for f, X, label in zip(f_list, X_list, labels):
            ax.plot(f, np.abs(X), label=label)
        ax.set_xticks(ticks)
        ax.set_xlabel("f, Гц")
        ax.set_ylabel("|X(f)|")
        ax.legend()

    def draw_arg(ax):
        for f, X, label in zip(f_list, X_list, labels):
            ax.plot(f, _get_phase(X), label=label)
        ax.set_xticks(ticks)
        ax.set_xlabel("f, Гц")
        ax.set_ylabel("arg X(f), рад")
        ax.legend()

    show_subplots(
        draw_funcs=[draw_mod, draw_arg],
        titles=["Модуль спектра", "Аргумент спектра"],
        figsize=(8, 8),
    )


def task_1() -> None:
    """
    `Используя выражение для расчета спектра непериодического прямоугольного
    сигнала вычислить спектр сигнала длительностью τ = 2c в диапазоне
    частот (0 - 3 * 1/τ)`
    """
    A = 1
    tau = 2

    f = np.linspace(0, 3 / tau, 1000)
    X = A * tau * np.sinc(f * tau)

    ic(tau, 1 / tau)
    for fi in (0, 0.25, 0.5, 0.75, 1, 1.5):
        ic(fi, A * tau * np.sinc(fi * tau))

    _draw_spectra(
        f_list=[f],
        X_list=[X],
        labels=[f"τ={tau}"],
        ticks=np.arange(0, 3 / tau + 0.01, 1 / tau),
    )


def task_2() -> None:
    """
    `Сформируйте непериодический прямоугольный сигнал с заданной
    длительностью τ. Проведите вычисление преобразования Фурье в виде
    численного интегрирования по формуле прямого преобразования Фурье в 2-3
    точках спектра. Вычислите и изобразите модуль и аргумент спектральной
    функции в интервале частот (0 - 3 * 1/τ).`
    """
    A = 1
    tau = 2

    t = _get_time_axis()
    x_t = get_single_rect_oscillation(a=A, tau=tau)(t)

    for fi in (0, 0.25, 0.75):
        X = get_fourier_transform(x_t, t, fi)
        ic(fi, X, abs(X), A * tau * np.sinc(fi * tau))

    f = np.linspace(0, 3 / tau, 300)
    X = _get_spectrum(x_t, t, f)

    _draw_spectra(
        f_list=[f],
        X_list=[X],
        labels=[f"τ={tau}"],
        ticks=np.arange(0, 3 / tau + 0.01, 1 / tau),
    )


def task_3() -> None:
    """
    `Вычислите и изобразите модуль и аргумент спектральной функции
    прямоугольного сигнала в интервале частот (0 - 3 * 1/τ). Измените
    длительность сигнала. Можно увеличить и уменьшить τ в 2 раза.
    Повторите вычисление спектра сигнала. При выводе графиков спектра
    выполните разметку оси частот. Сравните параметры спектра при
    изменении длительности сигнала.`
    """
    A = 1
    t = _get_time_axis()

    f_list = []
    X_list = []
    labels = []

    for tau in (1, 2, 4):
        x_t = get_single_rect_oscillation(a=A, tau=tau)(t)
        f = np.linspace(0, 3, 600)
        X = _get_spectrum(x_t, t, f)
        ic(tau, abs(X[0]), 1 / tau)
        f_list.append(f)
        X_list.append(X)
        labels.append(f"τ={tau}")

    _draw_spectra(
        f_list=f_list,
        X_list=X_list,
        labels=labels,
        ticks=np.arange(0, 3.01, 0.25),
    )


def task_4() -> None:
    """
    `Сформируйте непериодический прямоугольный сигнал с заданной
    длительностью τ. Проведите вычисления преобразования Фурье в виде
    численного интегрирования по формуле прямого преобразования Фурье.
    Изобразите модуль и аргумент спектральной функции в интервале частот
    (0 - 3 * 1/τ). Получите задержанный (смещенный) на τ0 прямоугольный
    сигнал. Проведите вычисления преобразования Фурье в виде численного
    интегрирования по формуле прямого преобразования Фурье. Изобразите
    модуль и аргумент спектральной функции в интервале частот
    (0 - 3 * 1/τ). Сделайте выводы по свойствам спектров.`
    """
    A = 1
    tau = 2
    tau0 = 1

    t = _get_time_axis()
    f = np.linspace(0, 3 / tau, 300)

    x_t = get_single_rect_oscillation(a=A, tau=tau)(t)
    x_delayed = get_single_rect_oscillation(a=A, tau=tau, t0=tau0)(t)

    X = _get_spectrum(x_t, t, f)
    X_delayed = _get_spectrum(x_delayed, t, f)

    ic(np.max(np.abs(np.abs(X) - np.abs(X_delayed))))
    ic(np.max(np.abs(X_delayed - X * np.exp(-2j * np.pi * f * tau0))))

    _draw_spectra(
        f_list=[f, f],
        X_list=[X, X_delayed],
        labels=["x(t)", f"x(t - {tau0})"],
        ticks=np.arange(0, 3 / tau + 0.01, 1 / tau),
    )


def task_5() -> None:
    """
    `Сформируйте непериодический прямоугольный сигнал с заданной
    длительностью τ. Проведите вычисления преобразования Фурье в виде
    численного интегрирования по формуле прямого преобразования Фурье.
    Изобразите модуль и аргумент спектральной функции в интервале частот
    (0 - 3 * 1/τ). Сформируйте отрезок гармонического колебания.
    Перемножьте колебание и прямоугольный сигнал. Повторите вычисление
    спектральной функции произведения сигналов с учетом частоты
    колебания. Изобразите модуль и аргумент спектральной функции.`
    """
    A = 1
    tau = 2
    f0 = 5

    t = _get_time_axis()
    x_t = get_single_rect_oscillation(a=A, tau=tau)(t)
    carrier = get_harmonic_oscillation(a=1, f=f0, phi=0, wave=np.cos)(t)
    x_mod = x_t * carrier

    f = np.linspace(0, 3 / tau, 300)
    X = _get_spectrum(x_t, t, f)

    f_mod = np.linspace(f0 - 3 / tau, f0 + 3 / tau, 600)
    X_mod = _get_spectrum(x_mod, t, f_mod)

    i_max = np.argmax(np.abs(X_mod))
    ic(f0, f_mod[i_max], abs(X_mod[i_max]), A * tau / 2)

    _draw_spectra(
        f_list=[f],
        X_list=[X],
        labels=["x(t)"],
        ticks=np.arange(0, 3 / tau + 0.01, 1 / tau),
    )
    _draw_spectra(
        f_list=[f_mod],
        X_list=[X_mod],
        labels=[f"x(t)cos(2π·{f0}t)"],
        ticks=np.arange(f0 - 3 / tau, f0 + 3 / tau + 0.01, 1 / tau),
    )


def main() -> None:
    task_1()
    print("-" * 50)
    task_2()

    print("-" * 50)
    task_3()

    print("-" * 50)
    task_4()
    print("-" * 50)
    task_5()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
