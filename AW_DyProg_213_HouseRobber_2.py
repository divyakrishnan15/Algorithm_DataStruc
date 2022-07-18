class Solution():
    def rob(self,nums):
            print("-----ROB-------")
            print("nums[0] =",nums[0])
            print("self.helper(nums[1:]) =",self.helper(nums[1:]))
            print("self.helper(nums[:-1]) =",self.helper(nums[:-1]))
            return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
            
    def helper(self, nums):
        rob1, rob2 = 0, 0
        
        for n in nums:
            print("-----HELPER------")
            print("n =",n)
            print("rob1 =",rob1)
            print("rob2 =",rob2)
            print("n + rob1 =",n + rob1)
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

nums = [1,2,3,1]
a=Solution()
print(a.rob(nums))

# Example 1:
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 3:
# Input: nums = [1,2,3]
# Output: 3