#Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.

def maxSubArray(A):
    maxsum = cursum = A[0]
    for a in A[1:]:
        cursum = max(cursum + a, a)
        maxsum = max(cursum, maxsum)
    return maxsum



print maxSubArray([-2,-1,1,6])
