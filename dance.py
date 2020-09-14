import uuid

import matplotlib.animation as animation
import matplotlib.pyplot as mplt
import numpy as np


mplt.style.use("dark_background")
figure = mplt.figure()
axes = mplt.axes(xlim=(0, 35), ylim=(0, 15))
(line,) = axes.plot([], [], lw=2)


def init():
    line.set_data([], [])
    return (line,)


xdata = [x for x in range(36)]#np.arange(0, 35)

ydata = []


def animate(_):
    ydata = [int(i, 16) for i in str(uuid.uuid4()).replace("-", "0")]
    line.set_data(xdata, ydata)
    return (line,)


dance = animation.FuncAnimation(
    figure, animate, init_func=init, frames=500, interval=20, blit=True
)
mplt.axis("off")
mplt.show()
