#Given an array nums, write a function to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.

def moveZerosToEnd(arr):
    outputArr = []
    if len(arr) == 0:
        return outputArr

    cnt = 0
    for x in arr:
        if x == 0:
            outputArr.append(x)
        else:
            cnt+=1

    for x in range(cnt):
        outputArr.append(0)

    return outputArr

arr = [1,-1,2,4,6]
