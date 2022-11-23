from timeit import Timer, timeit
from random import choice

def bubbleSort(items):
    for i in range(len(items)-1,0,-1): # generate a range for the next step
        for j in range(i):             # note that the range i is decrementing
            if items[ j] > items[j+1]:
                items[ j], items[j+1] = items[j+1], items[ j] # swap items

list_ = list(range(0,500))      # list of numbers
d1 = [choice(list_) for i in range(10)]  # random list of size 10
d2 = [choice(list_) for i in range(20)]  # random list of size 20

# you need to add more lists of different sizes: d3, d4, d5, and d6
data = [d1, d2]  # your input
times = []       # times required to sort input

for i in data:
    t1 = Timer(f"bubbleSort({i})", "from __main__ import bubbleSort")
    print("bubblesort ",t1.timeit(number=3), "milliseconds") # for debugging
    times.append(?) # record the time required to sort the input

# do not forget to plot your data!!!