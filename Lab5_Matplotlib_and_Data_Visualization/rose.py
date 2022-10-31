# create a rose curve in polar coordinates and
# add widgets that can control the curve parameters
# such as buttons and sliding bars

from matplotlib import pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import numpy as np
import random

def update(val):
    n = slider1.val
    d = slider2.val
    r = np.cos(theta * n / d)
    ax.cla()
    colors = ['slateblue', 'mediumslateblue', 'mediumpurple', 'darkorchid', 'darkviolet']
    line = ax.plot(theta+(r<0)*np.pi, np.abs(r), colors[random.randint(0,4)], linewidth=1)

# main
fig = plt.figure(figsize=(8,8))

ax = fig.add_subplot(1, 1, 1, polar=True)
ax.set_title("Rose Curve", pad = 20)

n, d = 3, 9
# you may need to adjust the theta range and increase the resolution (600)
theta = np.linspace(0, d/n*16*np.pi, 600)
# you may need to convert negative values of r into positive values
r = np.cos(theta * n / d)
line = ax.plot(theta+(r<0)*np.pi, np.abs(r), 'purple', linewidth=1)

plt.subplots_adjust(left=0.25, bottom=0.25)
slider1_ax = plt.axes([0.25, 0.15, 0.65, 0.03])
slider2_ax = plt.axes([0.25, 0.1, 0.65, 0.03])
slider1 = Slider(slider1_ax,'n value',0,13,valinit=n,valfmt="%i",valstep=1)
slider2 = Slider(slider2_ax,'d value',1,12,valinit=d,valfmt="%i",valstep=1)
slider1.on_changed(update)
slider2.on_changed(update)

plt.show()