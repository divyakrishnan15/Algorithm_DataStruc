def isPalindrome(s):
    newStr=""

    for i in s:
        if i.isalnum():
            newStr += i.lower()
            # if newStr == newStr[::-1]:
            #     return True
            # else:
            #     return False
            return newStr == newStr[::-1]
s="race a car"
#"racecar"
#res=isPalindrome(s)
print(isPalindrome(s))

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.