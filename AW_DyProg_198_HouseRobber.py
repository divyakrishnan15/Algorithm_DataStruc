def rob(nums):
    rob1, rob2 = 0, 0
    
    for n in nums:
        print("------------")
        print("n =",n)
        print("rob1 =",rob1)
        print("rob2 =",rob2)
        print("n + rob1 =",n + rob1)
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

nums = [1,2,3,1]
print(rob(nums))

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.