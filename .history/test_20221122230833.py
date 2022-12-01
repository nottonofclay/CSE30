# counting sort for digits 0 - 9

def countSort(arr):
    # count the same digits and put their counts at index = digit
    counts = [0 for i in range(11)]
    print(len(arr))
    for i in arr:
        counts[ i] += 1
    # convert counts into ranking: each index value = (number of items <= i)
    for i in range(10):
        counts[ i] += counts[ i-1]

    output = [0 for i in range(len(arr))]
    # use ranking as index and index as values
    for i in range(len(arr)-1, -1, -1):
        print(i,arr[ i],counts[arr[ i]])
        output[counts[arr[ i]]-1] = arr[ i]
        counts[arr[ i]] -= 1

    return output

# Driver program to test above function
arr = [1,6,7,0,9,3,4,5,4,2,3,6,3]
ans = countSort(arr)
print(f"Sorted array is {ans}")