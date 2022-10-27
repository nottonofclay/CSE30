from matplotlib import pyplot as plt
import numpy as np
arr = np.array([1, 2, 3, 4, 5])


arr_to2D = arr.reshape(5,1)
print(arr_to2D)
print(arr_to2D.reshape(-1))