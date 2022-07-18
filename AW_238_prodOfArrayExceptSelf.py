from operator import index


def prodofArrayExceptSelf(nums):
    res=[1]*len(nums)
    print("res = ",res)

    prefix=1
    for i in range(len(nums)):
        res[i]=prefix
        print("---PRE FIX----")
        print("res[i] = ",res[i])
        prefix*=nums[i]
        print("nums[i] = ",nums[i])
        print("prefix = ",prefix)
    postfix=1
    for i in range(len(nums)-1,-1,-1):
        res[i]=postfix
        print("---POSTFIX----")
        print("res[i] = ",res[i])
        postfix*=nums[i]
        print("nums[i] = ",nums[i])
        print("postfix = ",postfix)
    return res

nums = [1,2,3,4]
print(prodofArrayExceptSelf(nums))

# for i in range(len(nums)) = 1,2,3,4
# for i in nums             = values in list
# i = position/index
# list[i] = value if i (data)

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer =