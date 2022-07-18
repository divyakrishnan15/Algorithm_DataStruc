def coinchange(coins,amount):
    dp=[amount+1]*(amount+1)
    print("[amount+1] = ",[amount+1])
    print("(amount+1) = ",(amount+1))
    print("dp = ",dp)
    dp[0]=0

    for i in range(1,amount+1):
        for j in coins:
            print("i = ",i)
            print("j = ",j)
            if i-j >=0:
                print("dp[i] = ",dp[i])
                print("dp[i-j] = ",dp[i-j])
                dp[i]=min(dp[i],1+dp[i-j])
    return dp[amount] if dp[amount] != amount+1 else -1

coins=[1,2,5]
amount=11
print(coinchange(coins,amount))

#Ans=3

# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0
 

# Constraints:
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104