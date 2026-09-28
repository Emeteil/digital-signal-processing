from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from icecream import ic  # noqa: F401

import numpy as np
import utils.debug  # noqa: F401

from utils.harmonic import (
    get_harmonic_oscillation,
    get_rect_oscillation,
)
from utils.plotting import show_subplots, show_multi_plot
from utils.sampling import get_linspace
from utils.fourier import get_a, get_b, integrate


def _harmonic_fourier_spectrum(A: float, f: float, phi: float, n_harm: int = 4) -> None:
    fs = 2000
    start, stop = 0, 1 / f

    t = get_linspace(start=start, stop=stop, fs=fs)
    x_t = get_harmonic_oscillation(a=A, f=f, phi=phi, wave=np.cos)(t)

    n_range = range(n_harm + 1)

    a_n = np.array([get_a(n, x_t, t, f) for n in n_range])
    b_n = np.array([get_b(n, x_t, t, f) for n in n_range])

    for i in range(len(a_n)):
        if abs(a_n[i]) < 1e-9:
            a_n[i] = 0
        if abs(b_n[i]) < 1e-9:
            b_n[i] = 0

    ic(phi, a_n, b_n)

    A_n = np.sqrt(a_n**2 + b_n**2)
    phi_n = np.arctan2(-b_n, a_n)

    n_vals = np.array(list(n_range))

    def draw_signal(ax):
        ax.plot(t, x_t)
        ax.set_title(f"x(t), A={A}, f={f}, phi={phi:.3f}")
        ax.set_xlabel("t")
        ax.set_ylabel("x(t)")

    def draw_amp(ax):
        ax.stem(n_vals, A_n)
        ax.set_title("Спектр амплитуд A_n")
        ax.set_xlabel("n")
        ax.set_ylabel("A_n")

    def draw_phase(ax):
        ax.stem(n_vals, phi_n)
        ax.set_title("Спектр фаз phi_n")
        ax.set_xlabel("n")
        ax.set_ylabel("phi_n, рад")

    show_subplots(
        draw_funcs=[draw_signal, draw_amp, draw_phase],
        titles=["Сигнал", "Амплитуды", "Фазы"],
        figsize=(8, 9),
    )


def task_1() -> None:
    """
    `Задайте гармоническое колебание x(t), выберите значение амплитуды,
    частоты, начальную фазу задайте равной 0. Вычислите коэффициенты an и
    bn для n = 0,1,2,3,4. По полученным коэффициентам вычислите и постройте
    графики An, ф(n).`
    """
    _harmonic_fourier_spectrum(A=3, f=10, phi=0)


def task_2() -> None:
    """
    `Измените начальную фазу колебания и повторите вычисления.`
    """
    _harmonic_fourier_spectrum(A=3, f=10, phi=np.pi / 4)


def task_3() -> None:
    """
    `Сформируйте периодический прямоугольный сигнал с заданным периодом T
    и длительностью τ. Проведите вычисления коэффициентов ряда Фурье
    интегрированием произведения сигнала на опорные колебания. По
    полученным коэффициентам an и bn вычислить коэффициенты ряда Фурье в
    тригонометрической форме An и φn. Изобразите спектры амплитуд и фаз до
    6 гармоники. Выполните синтез временного колебания путем суммирования
    2, 4, 6 коэффициентов ряда Фурье и изобразите полученные временные
    колебания.`
    """
    fs = 5000
    T = 0.1
    tau = 0.05
    f0 = 1 / T
    N_HARM = 6

    t = get_linspace(start=0, stop=T, fs=fs)
    x_t = get_rect_oscillation(a=1, T=T, tau=tau)(t)

    n_range = range(N_HARM + 1)

    a_n = np.array([get_a(n, x_t, t, f0) for n in n_range])
    b_n = np.array([get_b(n, x_t, t, f0) for n in n_range])

    A_n = np.sqrt(a_n**2 + b_n**2)
    phi_n = np.arctan2(-b_n, a_n)
    n_vals = np.array(list(n_range))

    ic(a_n, b_n, A_n, phi_n)

    def draw_signal(ax):
        ax.plot(t, x_t)
        ax.set_title(f"x(t), T={T}, τ={tau}")
        ax.set_xlabel("t")
        ax.set_ylabel("x(t)")

    def draw_amp(ax):
        ax.stem(n_vals, A_n)
        ax.set_title("Спектр амплитуд A_n")
        ax.set_xlabel("n")
        ax.set_ylabel("A_n")

    def draw_phase(ax):
        ax.stem(n_vals, phi_n)
        ax.set_title("Спектр фаз phi_n")
        ax.set_xlabel("n")
        ax.set_ylabel("phi_n, рад")

    show_subplots(
        draw_funcs=[draw_signal, draw_amp, draw_phase],
        titles=["Сигнал", "Амплитуды", "Фазы"],
        figsize=(8, 9),
    )

    t_synth = get_linspace(start=0, stop=3 * T, fs=fs * 3)
    func_vals = []
    labels = []

    for n_max in (2, 4, 6):
        x_synth = np.full_like(t_synth, a_n[0] / 2)
        for n in range(1, n_max + 1):
            x_synth = x_synth + a_n[n] * np.cos(2 * np.pi * n * f0 * t_synth)
            x_synth = x_synth + b_n[n] * np.sin(2 * np.pi * n * f0 * t_synth)
        func_vals.append(x_synth)
        labels.append(f"N = {n_max}")

    show_multi_plot(
        t=t_synth,
        func_vals=func_vals,
        labels=labels,
        title="синтез прямоугольного сигнала суммой гармоник ряда Фурье"
    )


def task_4() -> None:
    """
    `Сформируйте сигнал s1(t) = sin(2πf1t) с частотой f1 = 1/T. Сформируйте
    сигнал sn(t) = sin(2πnf1t) и вычислите интеграл ∫s1(t)sn(t)dt.
    Проверьте, что интеграл ∫sk(t)sn(t)dt = 0 для всех положительных k и n.
    Измените значение частоты одного из колебаний и снова проверьте
    выполнение свойства ортогональности. Измените интервал интегрирования
    на несколько точек, проверьте выполнение свойства ортогональности.`
    """
    fs = 2000
    T = 1
    f1 = 1 / T

    t = get_linspace(start=0, stop=T, fs=fs)
    s1 = get_harmonic_oscillation(1, f1, 0, wave=np.sin)(t)

    for n in range(1, 6):
        sn = get_harmonic_oscillation(1, n * f1, 0, wave=np.sin)(t)
        result = integrate(s1 * sn, t)
        ic(n, result)

    ic("меняем частоту sn на не кратную f1")
    sn_off = get_harmonic_oscillation(1, 2.3 * f1, 0, wave=np.sin)(t)
    ic(integrate(s1 * sn_off, t))

    ic("сокращаем интервал интегрирования")
    t_short = get_linspace(start=0, stop=T / 4, fs=fs // 4)
    s1_short = get_harmonic_oscillation(1, f1, 0, wave=np.sin)(t_short)
    s3_short = get_harmonic_oscillation(1, 3 * f1, 0, wave=np.sin)(t_short)
    ic(integrate(s1_short * s3_short, t_short))


def task_5() -> None:
    """
    `Сформируйте сигнал sn(t) = e^(j(2πnf1t)) и вычислите интеграл
    ∫s1(t)sn(t)dt. Проверьте, что интеграл ∫sk(t)sn(t)dt = 0 для
    положительных и отрицательных k и n. На выбор номера n и к меняйте в
    пределах до 10. Измените значение частоты одного из колебаний и снова
    проверьте выполнение свойства ортогональности. Измените интервал
    интегрирования на несколько точек, проверьте выполнение свойства
    ортогональности.`
    """
    fs = 2000
    T = 1
    f1 = 1 / T

    t = get_linspace(start=0, stop=T, fs=fs)

    def s(n: float, freq: float, t: np.ndarray) -> np.ndarray:
        return np.exp(1j * 2 * np.pi * n * freq * t)

    for k, n in [(1, 1), (2, 3), (-2, 3), (4, -4), (10, -10), (5, 7)]:
        result = integrate(s(k, f1, t) * s(n, f1, t), t)
        ic(k, n, result)

    ic("меняем частоту sn на не кратную f1")
    ic(integrate(s(3, f1, t) * s(-3, 1.5 * f1, t), t))

    ic("сокращаем интервал интегрирования")
    t_short = get_linspace(start=0, stop=T / 4, fs=fs // 4)
    ic(integrate(s(3, f1, t_short) * s(2, f1, t_short), t_short))


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
