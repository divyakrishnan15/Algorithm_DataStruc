def searchInsertPosi(list):
    l,r=0,len(list)-1

    while l<=r:
        mid = (l+r)//2

        if target == list[mid]:
            return mid
        if target > list[mid]:
            l=mid+1
        else:
            r=mid-1
    return l

list =[1,3,5,6]
target = 5
res=searchInsertPosi(list)
print(res)

#Ans=1st position = 1

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104
