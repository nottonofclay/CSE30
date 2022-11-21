def selectionSort(items):
   counter = 1
   for i in range(len(items)-1,0,-1):
       m=0
       for j in range(1,i+1):          # find the maximum in the range
           if items[ j] > items[ m]:
               m = j
       items[ m], items[ i] = items[ i], items[ m]
       print(counter, items[m], items[i])

list_ = [54,26,93,17,77,31,44,55,20]
selectionSort(list_)
print(list_)