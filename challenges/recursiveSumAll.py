# add up all of the values inside the list

def sumAll(nums):
    if not nums:
        return 0
    
    #Using Recursion
    return nums[0] + sumAll(nums[1:])



print(sumAll([4, 8, 5, 2, 9])) # 28