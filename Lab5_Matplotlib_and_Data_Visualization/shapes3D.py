import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure()
ax = plt.axes(projection='3d')
x = [0, 0.5,1, 1, 0.5, 0, 1, 0, 0, 1]
y = [0, 0.5,0, 1, 0.5, 1, 1, 1, 0, 0]
z = [0, 1,  0, 0, 1,   0, 0, 0, 0, 0]

ax.plot3D(x,y,z)
plt.show()