import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 1.5 * np.pi, 0.01)
line, = ax.plot(x, np.tan(x), color='purple')


def animate(i):
    line.set_ydata(np.tan(x * 100 + i / 10))  # update the data.
    return line,


ani = animation.FuncAnimation(
    fig, animate, interval=10, blit=True, save_count=60)

plt.show()
