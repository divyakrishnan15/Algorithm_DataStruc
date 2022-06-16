def moveZeroes(self,nums):
    j = 0
    for i in nums:
        if(i != 0):
            nums[j] = i
            j += 1

    for x in range(j, len(nums)):
        nums[x] = 0

nums = [1,2,0,3]
print(moveZeroes(nums))