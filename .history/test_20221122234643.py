def bubbleSort(items):
    for i in range(len(items)-1,0,-1): # generate a range for the next step
        for j in range(i):             # note that the range i is decrementing
            if items[ j] > items[j+1]:
                items[ j], items[j+1] = items[j+1], items[ j] # swap items
                print([j], [j+1])

list_ = [54,26,93,17,77,31,44,55,20]
bubbleSort(list_)
print(list_)
