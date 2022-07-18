def longestPalindromeSubString(s):
        res = ""
        resLen = 0
        
        for i in range(len(s)):
            # odd length
            l, r = i, i
            print("-----------")
            print("res = ",res)
            print("resLen = ",resLen)
            print("l = ",l)
            print("list[l] = ",list[l])
            print("r = ",r)
            print("list[r] = ",list[r])
            while l >= 0 and r < len(s) and s[l] == s[r]:
                print("(r - l + 1) = ",(r - l + 1))
                print("resLen = ",resLen)
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    print("ODD = s[l:r+1] = ",s[l:r+1])
                    resLen = r - l + 1
                    print("ODD = resLen = ",resLen)
                l -= 1
                r += 1
            
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    print("EVEN = s[l:r+1] = ",s[l:r+1])
                    resLen = r - l + 1
                    print("ODD = resLen = ",resLen)
                l -= 1
                r += 1
                
        return res

s = "babad"
print(longestPalindromeSubString(s))

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"
 