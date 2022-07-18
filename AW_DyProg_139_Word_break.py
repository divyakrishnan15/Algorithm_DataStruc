def wordBreak(s, wordDict):
        
    dp = [False] * (len(s) + 1)
    print("dp = ",dp)
    dp[len(s)] = True
    
    for i in range(len(s) - 1, -1, -1):
        print("-----------")
        print("i = ",i)
        for w in wordDict:
            print("w = ",w)
            print("len(w) = ",len(w))
            print("len(s) = ",len(s))
            if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                dp[i] = dp[i + len(w)]
                print("if dp[i] = ",dp[i])
            if dp[i]:
                break
    print("if dp[0] = ",dp[0])
    return dp[0]


s = "applepenapple"
wordDict = ["apple","pen"]
print(wordBreak(s, wordDict))

# Example 1:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false