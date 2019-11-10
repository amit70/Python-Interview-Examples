# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.


def removeDuplicates(nums):
    index = 1
    
    while index <= len(nums) - 1:
        if nums[index - 1] == nums[index]:
            nums.pop(index)
        else:
            index+=1
    return len(nums)

print removeDuplicates([0,0,1,1,1,2,2,3,3,4])
