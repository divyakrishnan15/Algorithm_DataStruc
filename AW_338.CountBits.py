def countbits(n):
    #print("[0] = ",[0])
    #print("n =",n)
    dp=[0]*(n+1)
    #print("dp = ",dp)
    #print("===========")
    offset=1

    for i in range(1,n+1):
        #print("offset*2 =",offset*2)
        #print("i=",i)
        #print("offset = ",offset)
        if offset*2==i:
            offset=i
        dp[i]=1+dp[i-offset]
        #print("dp[i-offset] = ",dp[i-offset])
        #print("dp[i] = ",dp[i])
        #print("------------")
    return dp
n=5
print(countbits(n))

# Example 1:
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# Example 2:
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
 

# Constraints:
# 0 <= n <= 105