def mergeSort(items):
    print("Splitting ",items)
    if len(items)>1:
        mid = len(items)//2
        l = items[:mid]
        r = items[mid:]
        mergeSort(l)
        mergeSort(r)
        print("Merging ",items)
        i, j, k = 0, 0, 0
        while i < len(l) and j < len(r):
            if l[ i] <= r[ j]:
                items[ k] = l[ i]
                i += 1
            else:
                items[ k] = r[ j]
                j += 1
            k += 1
        while i < len(l):
            items[ k] = l[ i]
            i, k = i+1, k+1
        while j < len(r):
            items[ k] = r[ j]
            j, k = j+1, k+1

list_ = [54,26,93,17,77,31,44,55,20]
mergeSort(list_)
print(list_)