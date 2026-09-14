from typing import Callable, Sequence
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes


def show_multi_plot(
    t: np.ndarray,
    func_vals: Sequence[np.ndarray],
    labels: Sequence[str] | None = None,
    is_stem: bool = False,
    is_enable_ion: bool = False,
    title: str | None = None,
    on_axes: Callable[[Axes], None] | None = None
) -> None:
    if is_enable_ion:
        plt.ion()

    plt.figure()
    ax = plt.gca()

    for i, func_val in enumerate(func_vals):
        label = labels[i] if labels else None
        if is_stem:
            plt.stem(t, func_val, label=label)
        else:
            plt.plot(t, func_val, label=label)

    if title:
        plt.title(title)

    if on_axes:
        on_axes(ax)

    if labels:
        plt.legend()

    plt.grid()

    try:
        plt.show()
    except KeyboardInterrupt:
        pass


def show_plot(
    t: np.ndarray,
    func_val: np.ndarray,
    is_stem: bool = False,
    is_enable_ion: bool = False,
    title: str | None = None,
    on_axes: Callable[[Axes], None] | None = None
) -> None:
    show_multi_plot(
        t=t,
        func_vals=[func_val],
        is_stem=is_stem,
        is_enable_ion=is_enable_ion,
        title=title,
        on_axes=on_axes
    )
