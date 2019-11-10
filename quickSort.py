#QuickSort

def partition(Arr,start,end):
    pIndex = start
    pivot = Arr[end]
    i = start

    while(i<end):
        if Arr[i] <= pivot:
            swap(Arr,i,pIndex)
            pIndex+=1
        i += 1
    swap(Arr,pIndex,end)
    return pIndex

def swap(Arr, value1,value2):
    temp = Arr[value1]
    Arr[value1] = Arr[value2]
    Arr[value2] = temp

Arr=[7,2,1,6,8,5,3,4]
print quickSort(Arr,0,len(Arr)-1)
