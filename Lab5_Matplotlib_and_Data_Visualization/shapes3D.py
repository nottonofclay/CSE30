import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure()
points = [3,3,3]
data = np.ones(points)
ax = fig.add_subplot(111, projection='3d')
ax.voxels(data)
plt.show()