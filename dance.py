import sys
from typing import Any, List, Tuple
import uuid

import matplotlib.animation as animation
from matplotlib.lines import Line2D
from matplotlib import pyplot


def uuid_as_list() -> List[int]:
    """Returns a list of integers each representing a symbol of random UUID.
    Dashes are replaced with zeros.
    """
    return [int(i, 16) for i in str(uuid.uuid4()).replace("-", "0")]


pyplot.style.use("dark_background")

figure = pyplot.figure()
axes = pyplot.axes(xlim=(0, 35), ylim=(0, 15))
(line_3,) = axes.plot([], [], linewidth=0.5, color="#000BF5", drawstyle="steps-mid")
(line_2,) = axes.plot([], [], linewidth=1.0, color="#0085F5", drawstyle="steps-mid")
(line_1,) = axes.plot([], [], linewidth=2.0, color="#00F5EA", drawstyle="steps-mid")

uuid_queue = [uuid_as_list()] * 3
x_data = [x for x in range(36)]


def init() -> Tuple[Line2D]:
    """Animation init.
    Only required for blitting to give a clean slate."""
    line_1.set_data([], [])
    line_2.set_data([], [])
    line_3.set_data([], [])
    return (line_3, line_2, line_1)


def animate(_: Any) -> Tuple[Line2D]:
    """Animation frame."""
    line_1.set_data(x_data, uuid_queue.pop(0))
    line_2.set_data(x_data, uuid_queue[0])
    line_3.set_data(x_data, uuid_queue[1])
    uuid_queue.append(uuid_as_list())
    return (line_3, line_2, line_1)


pyplot.axis("off")
dance = animation.FuncAnimation(
    figure,
    animate,
    init_func=init,
    frames=None,
    interval=100,
    save_count=100,
    blit=True,
)

if sys.argv[1] == "save":
    dance.save(sys.argv[2] + ".gif", writer="imagemagick")
elif sys.argv[1] == "show":
    pyplot.show()
