from collections import defaultdict

def containsDuplicate(nums):
    dict = defaultdict(int)

    for i in nums:
        if dict[i]:
            return True,i
        dict[i]+=1
    return False

nums=[1,2,3,4,2,1]
print(containsDuplicate(nums))


# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 

# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
