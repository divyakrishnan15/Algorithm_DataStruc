def maxsubarray(nums):
    maxsub=nums[0]
    print("nums[0] =",nums[0])
    currsum = 0

    for i in nums:
        print("i =============",i)
        if currsum < 0:
            currsum = 0 
        currsum +=i
        print("currsum =",currsum)
        print("maxsub ~~",maxsub)
        maxsub=max(maxsub,currsum)

    return maxsub

nums=[-2,1,-3,4,-1,2,1,-5,4]
res=maxsubarray(nums)
print(res)

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23