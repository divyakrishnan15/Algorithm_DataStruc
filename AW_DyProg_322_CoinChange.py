def coinChange(coins, amount):
        dp = [amount + 1] * (amount + 1) 
        
        print("[amount + 1] = ",[amount + 1])
        print("(amount + 1) = ",(amount + 1))
        dp[0] = 0
        
        for a in range(1, amount + 1):
            print("--------------")
            print("a = ",a)
            for c in coins:
                print("c =",c)
                if a - c >= 0:
                    print("dp[a] = ",dp[a])
                    print("dp[a - c] = ",dp[a - c])
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    print("dp[amount] = ",dp[amount])
        return dp[amount] if dp[amount] != amount + 1 else -1

coins = [1,2,5]
amount = 11
print(coinChange(coins, amount))

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