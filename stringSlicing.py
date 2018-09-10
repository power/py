def multiplyList(nums):
    for i in range (len(nums)):
        nums[i] = (nums[i]*5)
    return nums

print (multiplyList(([1,2,3,4,5])))
