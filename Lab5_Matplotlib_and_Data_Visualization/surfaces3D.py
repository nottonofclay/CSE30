import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

fig = plt.figure()

# hyperbolic paraboloid
ax = fig.add_subplot(3, 3, 1, projection='3d')
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x, y)
Z = X**2 - Y**2
ax.contour3D(X, Y, Z, 50, cmap='plasma')
ax.set_title('Hyperbolic Paraboloid')

# elliptic paraboloid
ax = fig.add_subplot(3, 3, 2, projection='3d')
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x,y)
Z = X**2 + Y**2
ax.contour3D(X, Y, Z, 50, cmap='plasma')
ax.set_title('Elliptic Paraboloid')

# hyperbolic hyperboloid
ax = fig.add_subplot(3, 3, 3, projection='3d')
r = 1
u = np.linspace(-1, 1, 100)
v = np.linspace(0, 2*np.pi, 60)
[u,v] = np.meshgrid(u, v)
X = np.cosh(u) * np.cos(v)
Y = np.cosh(u) * np.sin(v)
Z = np.sinh(u)
ax.contour3D(X, Y, Z, 50, cmap='plasma')
ax.set_title('Hyperbolic Hyperboloid')

# elliptical hyperboloid
ax = fig.add_subplot(3, 3, 4, projection='3d')
u = np.linspace(-1, 1, 100)
v = np.linspace(0, 2*np.pi, 60)
[u,v] = np.meshgrid(u, v)
X = np.sinh(u) * np.cos(v)
Y = np.sinh(u) * np.sin(v)
Z = np.cosh(u)
ax.contour3D(X, Y, Z, 50, cmap='plasma')
u = np.linspace(-1, 1, 100)
v = np.linspace(0, 2*np.pi, 60)
[u,v] = np.meshgrid(u, v)
X = np.sinh(u) * np.cos(v)
Y = np.sinh(u) * np.sin(v)
Z = -np.cosh(u)
ax.contour3D(X, Y, Z, 30, cmap='plasma')
ax.set_title('Elliptic Hyperboloid')

# sphere
ax = fig.add_subplot(3, 3, 5, projection='3d')
u = np.linspace(-1, 1, 100)
v = np.linspace(0, 2*np.pi, 60)
[u,v] = np.meshgrid(u, v)
X = np.sqrt(1 - u**2) * np.cos(v)
Y = np.sqrt(1 - u**2) * np.sin(v)
Z = np.sin(u)
ax.contour3D(X, Y, Z, 50, cmap='plasma')
ax.set_title('Sphere')

# cone
ax = fig.add_subplot(3, 3, 6, projection='3d')
u = np.linspace(-1, 1, 100)
v = np.linspace(0, 2*np.pi, 60)
[u,v] = np.meshgrid(u, v)
X = ((1-u) / 1) * np.cos(v)
Y = ((1-u) / 1) * np.sin(v)
Z = np.sin(u)
ax.contour3D(X, Y, Z, 50, cmap='plasma')
ax.set_title('Cone')

# square pyramid
ax = fig.add_subplot(3, 3, 7, projection='3d')
points = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0.5, 0.5, 1]])
X = points[ : ,0]
Y = points[ : ,1]
Z = points[ : ,2]
ax.plot_trisurf(X, Y, Z, cmap='plasma')
ax.set_title('Square Pyramid')

# parallelepiped
ax = fig.add_subplot(3, 3, 9, projection='3d')
points = np.array([[-1, -1, -1],
                  [1, -1, -1 ],
                  [1, 1, -1],
                  [-1, 1, -1],
                  [-1, -1, 1],
                  [1, -1, 1 ],
                  [1, 1, 1],
                  [-1, 1, 1]])

P = [[2.06498904e-01 , -6.30755443e-07 ,  1.07477548e-03],
     [1.61535574e-06 ,  1.18897198e-01 ,  7.85307721e-06],
     [7.08353661e-02 ,  4.48415767e-06 ,  2.05395893e-01]]

Z = np.zeros((8,3))
for i in range(8): Z[i,:] = np.dot(points[i,:],P)
Z = 10.0*Z
X, Y = np.meshgrid(r, r)
# plot vertices
ax.scatter3D(Z[:, 0], Z[:, 1], Z[:, 2])

# list of sides' polygons of figure
verts = [[Z[0],Z[1],Z[2],Z[3]],
 [Z[4],Z[5],Z[6],Z[7]],
 [Z[0],Z[1],Z[5],Z[4]],
 [Z[2],Z[3],Z[7],Z[6]],
 [Z[1],Z[2],Z[6],Z[5]],
 [Z[4],Z[7],Z[3],Z[0]]]

# plot sides
ax.add_collection3d(Poly3DCollection(verts, facecolors='purple'))


plt.show()