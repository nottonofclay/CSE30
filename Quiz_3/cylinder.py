import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

def cylinder(a, b):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    u = np.linspace(-1, 1, 100)
    v = np.linspace(0, 2*np.pi, 60)
    [u,v] = np.meshgrid(u, v)
    X = a * np.cos(v)
    Y = a * np.sin(v)
    Z = b * u
    ax.contour3D(X, Y, Z, 50, cmap='plasma')
    ax.set_title('Cylinder')
    plt.show()

if __name__ == '__main__':
    cylinder(1, 2)
    cylinder(2, 10)
