def SearchinRotatedSortedArray(nums,target):
    l,r=0,len(nums)-1

    while l<=r:
        mid=(l+r)//2
        # print("------------")
        # print("l = ",l)
        # print("nums[l] = ",nums[l])
        # print("r = ",r)
        # print("nums[r] = ",nums[r])
        # print("mid = ",mid)
        # print("nums[mid] = ",nums[mid])
        if target==nums[mid]:
            return mid
        #left sorted postion
        if nums[l] <= nums[mid]:
            #print("nums[l] <= nums[mid] = ",nums[l] <= nums[mid])
            if target > nums[mid] or target<nums[l]:
                l=mid+1
                #print(" if l =",l)
            else:
                r=mid-1
                #print(" else r =",r)
        #right sorted postion
        else:
            if target < nums[mid] or target<nums[r]:
                r=mid-1
                #print(" else if r =",r)
            else:
                l=mid+1
                #print(" else else l =",l)
    return -1

nums=[4,5,6,7,0,1,2]
target=0
print(SearchinRotatedSortedArray(nums,target))

# Given the array nums after the possible rotation and 
# an integer target, return the index of target if 
# it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime 
# complexity.

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:
# Input: nums = [1], target = 0
# Output: -1
 
# Constraints:
# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104