def longestCommonSubsequence(text1, text2):
    dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
    
    print("[0 for j in range(len(text2) + 1)]=",[0 for j in range(len(text2) + 1)])
    for i in range(len(text1) - 1, -1, -1):
        pritn("-------------")
        print("i =",i)
        for j in range(len(text2) - 1, -1, -1):
            print("j =",j)
            print("text1[i] =",text1[i])
            print("text2[j] =",text2[j])
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
                print("dp[i][j] =",dp[i][j])
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
                print("dp[i][j] =",dp[i][j])
    return dp[0][0]