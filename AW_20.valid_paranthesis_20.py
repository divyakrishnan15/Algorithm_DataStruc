def validparanthesis(s):
    stack=[]
    closetoopen={")":"(","]":"[","}":"{"}

    for i in s:
        # print("-----------")
        # print("i = ",i)
        # print("s = ",s)
        if i in closetoopen:
            # print("stack = ",stack)
            # print("stack[-1] = ",stack[-1])
            # print("closetoopen[i] = ",closetoopen[i])
            if stack and stack[-1] == closetoopen[i]:
                stack.pop()
            else:
                return False
        else:
            #print("ELSE stack = ",stack)
            stack.append(i)

    return True if not stack else False

s="(){}[]"
res=validparanthesis(s)
print(res)

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false
             