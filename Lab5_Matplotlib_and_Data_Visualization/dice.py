import numpy as np
import matplotlib.pyplot as plt
import random

# results = {}
# for i in range(100):
#     throw = random.randint(1,6) + random.randint(1,6)
#     try:
#         results[throw] += 1
#     except:
#         results[throw] = 1

# results = dict(sorted(results.items()))

# keys   = list(results.keys())
# values = list(results.values())

results = []
for i in range(100):
    results.append(random.randint(1,6) + random.randint(1,6))

plt.hist()
plt.show()