def Min_Window_Substring(s,t):
    if t == "": return ""
    
    countT, window = {}, {}
    for c in t:
        countT[c] = 1 + countT.get(c, 0)
    print("-----------")
    print("countT[c] = ",countT[c])
    have, need = 0, len(countT)
    res, resLen = [-1, -1], float("infinity")
    l = 0
    for r in range(len(s)):
        
        print("countT = ",countT)
        print("window = ",window)
        print("l = ",l)
        print("r = ",r)
        print("s[r] = ",s[r])
        print("have = ",have)
        print("need = ",need)
        print("res = ",res)
        print("resLen = ",resLen)
        c = s[r]
        window[c] = 1 + window.get(c, 0)
        print("window[c] = ",window[c])
        if c in countT and window[c] == countT[c]:
            have += 1
    
        while have == need:
            # update our result
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = (r - l + 1)
            # pop from the left of our window
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l:r+1] if resLen != float("infinity") else ""

s="ADOBECODEBANC"
t="ABC"
print(Min_Window_Substring(s,t))

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.