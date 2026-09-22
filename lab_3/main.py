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
from utils.plotting import show_subplots, show_plot
from utils.sampling import get_linspace
from utils.fourier import get_a, get_b


def task_1() -> None:
    fs = 2000
    A = 3
    f = 10
    phi = 0
    start, stop = 0, 1 / 10

    t = get_linspace(start=start, stop=stop, fs=fs)
    x_t = get_harmonic_oscillation(a=A, f=f, phi=phi, wave=np.cos)(t)
    
    N_HARM = 4
    n_range = range(N_HARM + 1)

    a_n = np.array([get_a(n, x_t, t, f) for n in n_range])
    b_n = np.array([get_b(n, x_t, t, f) for n in n_range])

    for i in range(len(a_n)):
        if a_n[i] < 1e-9:
            a_n[i] = 0
            b_n[i] = 0

    ic(
        a_n,
        b_n
    )
    
    A_n = np.sqrt(a_n**2 + b_n**2)
    phi_n = np.arctan2(-b_n, a_n)

    n_vals = np.array(list(n_range))

    def draw_signal(ax):
        ax.plot(t, x_t)
        ax.set_title(f"x(t), A={A}, f={f}, phi={phi}")
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
    


def main() -> None:
    task_1()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
