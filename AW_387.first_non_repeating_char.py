def firstNonRepeatingChar(list):
    dict={}

    for i in range(len(list)):
        dict[list[i]]=1+dict.get(list[i],0)
        #print("dict[list[i]] = ",dict[list[i]])
        #print(dict)
        #countS[s[i]] = 1+countS.get(s[i],0)

    for j in dict:
        if dict[j]==1:
            return j,dict[j]

#list=['a','a','a','b','c','d','d','c']
list="leetcode"
print(firstNonRepeatingChar(list))


# Example 1:
# Input: s = "leetcode"
# Output: 0

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

# Example 3:
# Input: s = "aabb"
# Output: -1
 

# Constraints:
# 1 <= s.length <= 105
# s consists of only lowercase English letters.