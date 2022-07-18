def longSubWithourRepeatChar(s):
    res=0
    l=0

    MySet=set()

    for r in range(len(s)):
        print("-----------")
        print("l = ",l)
        print("s[l] = ",s[l])
        print("r = ",r)
        print("s[r] = ",s[r])
        while s[r] in MySet:
            print("MySet = ",MySet)
            print("remove = s[l] =",s[l])
            MySet.remove(s[l])
            print("MySet = ",MySet)
            l+=1
            print("l = ",l)
        print("added =  s[r] =",s[r])
        MySet.add(s[r])
        print("MySet = ",MySet)
        res=max(res,r-l+1)
    return res

def abc(s):
    print("---")
    print(set(s))
    print("------")

s="abcabcbb"

print(longSubWithourRepeatChar(s))
print(abc(s))
#Ans : abc = 3

# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.