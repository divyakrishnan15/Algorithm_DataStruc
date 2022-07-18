def MaxProdSubArray(nums):
    res=max(nums)
    curMin,curMax=1,1

    for i in nums:
        if i==0:
            curMin,curMax=1,1
            continue
        tmp=curMax*i
        print("tmp =",tmp)
        print("i =",i)
        print("curMin =",curMin)
        print("curMax =",curMax)
        curMax=max(i*curMax, i*curMin, i)
        curMin=min(tmp ,i*curMin, i)
        res=max(res,curMax)
        print("res =",res)
    return res
nums = [2,3,-2,4]
print(MaxProdSubArray(nums))

# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

# Constraints:
# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# Accepted
# 785,745
# Submissions
# 2,266,116