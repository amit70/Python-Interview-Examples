#MergerSort implementation

def merge(arr,helperArr,low,mid,high):
    for x in xrange(low, high + 1):
        helperArr[x] = arr[x]

    helperLeft = low
    helperRight = mid + 1
    current = low

    while helperLeft <= mid and helperRight <= high:
        if helperArr[helperLeft] <= helperArr[helperRight]:
            arr[current] = helperArr[helperLeft]
            helperLeft+=1
            current+=1
        else:
            arr[current] = helperArr[helperRight]
            helperRight+=1
            current += 1

    remaining = mid - helperLeft

    for x in range(0,remaining + 1):
        arr[current + x] = helperArr[helperLeft + x]


arr = [187,662,89,592,971,708,80,166]
helperArr = [None] * len(arr)
mergeSort(arr, helperArr,0, len(arr) - 1)
print arr
