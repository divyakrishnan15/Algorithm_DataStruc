class validpalindrome():
    def validpalindrome(self,s):
        l, r = 0, len(s) - 1
        while l < r:
            print("-----------")
            print("l = ",l)
            print("s[l] = ",s[l])
            print("r = ",r)
            print("s[r] = ",s[r])
            print("self.alphanum(s[l]): = ",self.alphanum(s[l]))
            print("self.alphanum(s[r]): = ",self.alphanum(s[r]))
            while l < r and not self.alphanum(s[l]): 
                l += 1
                print("2nd l = ",l)
            while l < r and not self.alphanum(s[r]): 
                r -= 1
                print("2nd r = ",r)
            print("s[l].lower() = ",s[l].lower())
            print("s[r].lower() = ",s[r].lower())
            if s[l].lower() != s[r].lower(): 
                return False
            l += 1
            r -= 1
        return True

    # Could write own alpha-numeric function
    def alphanum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

a=validpalindrome()
s = "A man, a plan, a canal: Panama"

print(a.validpalindrome(s))

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
 