def canJump(nums):
    goal = len(nums) -1
    
    for i in range(len(nums) - 2, -1, -1):
        print("i = ",i)
        print("nums[i] = ",nums[i])
        print("goal = ",goal)
        if i + nums[i] >= goal:
            goal = i
    return True if goal == 0 else False

nums = [2,3,1,1,4]
print(canJump(nums))

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, 
# then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 
# no matter what. Its maximum jump length is 0, 
# which makes it impossible to reach the last index.