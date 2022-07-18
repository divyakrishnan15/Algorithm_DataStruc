class Solution():
    def countSubstrings(self, s):
        res = 0        
        for i in range(len(s)):
            print("----- Count SUB STRING -----")
            res += self.countPali(s, i, i)
            print("self.countPali(s, i, i) = ",self.countPali(s, i, i))
            res += self.countPali(s, i, i + 1)
            print("self.countPali(s, i, i+1) = ",self.countPali(s, i, i+1))
        return res
    
    def countPali(self, s, l, r):
        res = 0
        print("****** Count Pali*****")
        print("l = ",l)
        print("s[l] = ",s[l])
        print("r = ",r)
        #print("s[r] = ",s[r])
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res

a=Solution()
str="aaa"
print(a.countSubstrings(str))

# Example 1:
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

# Constraints:
# 1 <= s.length <= 1000
# s consists of lowercase English letters.