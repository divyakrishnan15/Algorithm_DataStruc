def twosum(nums,target):
    hm={}
    for i,n in enumerate(nums):
        print("------------")
        print("i = ", i)
        print("n = ", n)
        print("hm = ",hm)
        diff = target-n
        if diff in hm:
            return (hm[diff],i),(diff,n)
        hm[n] = i
       
nums=[1,2,6,3,4,7]
target = 5

res =twosum(nums,target)
print(res)

####################
print("----------2 POINTER--------")
def isPairSum(arr, N, X):
  
    for i in range(N):
        for j in range(N):  
            # as equal i and j means same element
            if(i == j):
                continue  
            # pair exists
            if (arr[i] + arr[j] == X):
                return True,arr[i],arr[j]  
            # as the array is sorted
            if (arr[i] + arr[j] > X):
                break
  
    # No pair found with given sum
    return 0
  
  
# Driver code
arr=[1,2,6,3,4,7]
val=5
#arr = [2, 3, 5, 8, 9, 10, 11]
#val = 17
  
print(isPairSum(arr, len(arr), val))

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.