test = [1,2,3,4,5]

def multiplyList(nums):
    for i in range (len(nums)):
        nums[i] = (nums[i]*5)
    print ("The multiplied list is %s" % nums)
    high = max(nums)
    low = min(nums)
    print("The lowest number in the multiplied list is %d and the highest is %d" % (low, high))

multiplyList(test)
