from timeit import Timer, timeit
from random import choice
import matplotlib.pyplot as plt

def bubbleSort(items):
    for i in range(len(items)-1,0,-1): # generate a range for the next step
        for j in range(i):             # note that the range i is decrementing
            if items[ j] > items[j+1]:
                items[ j], items[j+1] = items[j+1], items[ j] # swap items

def selectionSort(items):
   for i in range(len(items)-1,0,-1):
       m=0
       for j in range(1,i+1):          # find the maximum in the range
           if items[ j] > items[ m]:
               m = j
       items[ m], items[ i] = items[ i], items[ m]

def quickSort(alist,first,last):
   if first<last:
       splitpoint = partition(alist,first,last)
       quickSort(alist,first,splitpoint-1)
       quickSort(alist,splitpoint+1,last)

def partition(alist,first,last):
   pivotvalue = alist[ first]
   leftmark = first+1
   rightmark = last
   done = False
   while not done:
       while leftmark <= rightmark and alist[ leftmark] <= pivotvalue:
           leftmark = leftmark + 1
       while alist[ rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1
       if rightmark < leftmark:
           done = True
       else:
           alist[ leftmark], alist[ rightmark] = alist[ rightmark],alist[ leftmark]
   alist[ first], alist[ rightmark] = alist[ rightmark], alist[ first]
   return rightmark

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
bubblesort_times = []       # times required to sort input
selectionsort_times = []
quicksort_times = []

for i in data:
    t1 = Timer(f"bubbleSort({i})", "from __main__ import bubbleSort")
    bubblesort_times.append(t1.timeit(number=3)) # record the time required to sort the input
    t2 = Timer(f"selectionSort({i})", "from __main__ import selectionSort")
    selectionsort_times.append(t2.timeit(number=3))
    t3 = Timer(f"quickSort({i})", "from __main__ import quickSort")
    quicksort_times.append(t3.timeit(number=3))

fig = plt.figure()
ax = fig.add_subplot(2, 2, 1)
ax.plot(sizes, bubblesort_times)
ax.title('Bubble Sort')

plt.show()
# do not forget to plot your data!!!