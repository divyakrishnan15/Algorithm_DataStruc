def containerwithmostwater(height):
    res=0
    l,r=0,len(height)-1

    while(l<r):
        print("-----------")
        print("l = ",l)
        print("height[l] = ",height[l])
        print("r = ",r)
        print("height[r] = ",height[r])
        area = (r-l) * min(height[l],height[r])
        print("area = ",area)
        res=max(res,area)
        print("res = ",res)

        if height[l] <height[r]:
            l+=1
        else:
            r-=1
    return res

height=[1,8,6,2,5,4,8,3,7]
print(containerwithmostwater(height))

#Ans = 7*7 = 49

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1
 
# Constraints:
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104