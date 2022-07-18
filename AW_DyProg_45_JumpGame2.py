def jumpgame2(nums):    
    l, r = 0, 0
    res = 0
    while r < (len(nums) - 1):
        print("----------")
        print("l = ",l)
        print("r = ",r)
        
        maxJump = 0
        for i in range(l, r + 1):
            print("i = ",i)
            print("maxJump = ",maxJump)
            print("nums[i] = ",nums[i])
            print("i + nums[i] = ",i + nums[i])
            maxJump = max(maxJump, i + nums[i])
        l = r + 1
        print("2nd l = ",l)
        r = maxJump
        print("2nd r = ",r)
        res += 1
    return res

nums = [2,3,1,1,4]
print(jumpgame2(nums))

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [2,3,0,1,4]
# Output: 2