from timeit import Timer, timeit
from random import choice
import matplotlib.pyplot as plt

def bubbleSort(items):
    for i in range(len(items)-1,0,-1): # generate a range for the next step
        for j in range(i):             # note that the range i is decrementing
            if items[ j] > items[j+1]:
                items[ j], items[j+1] = items[j+1], items[ j] # swap items

list_ = list(range(0,500))      # list of numbers
d1 = [choice(list_) for i in range(10)]  # random list of size 10
d2 = [choice(list_) for i in range(20)]  # random list of size 20
d3 = [choice(list_) for i in range(50)]  # random list of size 50
d4 = [choice(list_) for i in range(100)]  # random list of size 100
d5 = [choice(list_) for i in range(200)]  # random list of size 200
d6 = [choice(list_) for i in range(500)]  # random list of size 500

# you need to add more lists of different sizes: d3, d4, d5, and d6
data = [d1, d2, d3, d4, d5, d6]  # your input
sizes = [10, 20, 50, 100, 200, 500]
times = []       # times required to sort input

for i in data:
    t1 = Timer(f"bubbleSort({i})", "from __main__ import bubbleSort")
    duration = t1.timeit(number=3)
    print("bubblesort ",duration, "milliseconds") # for debugging
    times.append(duration) # record the time required to sort the input

print(times)

fig = plt.figure()
ax = fig.add_subplot(2, 2, 1)
ax.plot(sizes, times)
plt.show()
# do not forget to plot your data!!!