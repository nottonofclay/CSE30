# counting sort for digits 0 - 9
def count_sort(arr, pos, m):
    # count the same digits and put their counts at index = digit
    counts = [0 for i in range(11)]
    for i in arr:
        i = str(i)
        while len(i) < m: # add 0s in front to small numbers
            i = '0' + i
        i = int(i[ pos])
        counts[ i] += 1
    # convert counts into ranking: each index value = (number of items <= i)
    for i in range(10):
        counts[ i] += counts[ i-1]

    output = [0 for i in range(len(arr))]
    # use ranking as index and index as values
    for i in range(len(arr)-1, -1, -1):
        j = str(arr[ i])
        while len(j) < m:
            j = '0' + j
        j = int(j[ pos])
        output[counts[ j]-1] = arr[ i]
        counts[ j] -= 1

    return output

def radix_sort(arr, pos):
    for i in range(pos-1, -1, -1):
        arr = count_sort(arr,i,pos)
    return arr


# Driver program to test above function
arr = [11,103,10,16,23,27,10,19,13,14,4,123]
print(arr)
d = 3 # max digits in a number
ans = radix_sort(arr, d)
print(f"Sorted array is {ans}")