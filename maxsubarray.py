def maxsubarray(nums):
    maxsub=nums[0]
    currsum = 0

    for i in nums:
        if currsum < 0:
            currsum = 0

        currsum +=i

        maxsub=max(maxsub,currsum)

    return maxsub

nums=[-2,1,-3,4,-1,2,1,-5,4]
res=maxsubarray(nums)
print(res)