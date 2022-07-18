def longestIncSubSeq(nums):
        LIS = [1] * len(nums)
        
        for i in range(len(nums) - 1, -1, -1):
            print("---------------")
            print("i = ",i)
            for j in range(i + 1, len(nums)):
                print("j = ",j)
                print("nums[i] =",nums[i])
                print("nums[j] =",nums[j])
                if nums[i] < nums[j]:
                    print("LIS[i] =",LIS[i])
                    print("LIS[j] =",LIS[j])
                    print("1+ LIS[j] =",1+LIS[j])
                    LIS[i] = max(LIS[i], 1 + LIS[j])
                    print("Lis = ",LIS)
        return max(LIS)

nums = [10,9,2,5,3,7,101,18]
print(longestIncSubSeq(nums))


# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4

# Example 3:
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1