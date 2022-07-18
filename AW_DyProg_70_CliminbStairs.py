def climbStairs(n):
    if n <= 3: return n
    n1, n2 = 2, 3
    print("-----------")
    print("n1 = ",n1)
    print("n2 = ",n2)
    for i in range(4, n + 1):
        print("i = ",i)
        temp = n1 + n2
        print("temp = ",temp)
        n1 = n2
        n2 = temp
    return n2

n = 3
print(climbStairs(n))

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step