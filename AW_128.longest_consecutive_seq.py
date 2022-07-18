def longest_consecutive_seq(nums):
    numSet=set(nums)
    longest=0

    for i in nums:
        if (i-1) not in numSet:
            length=0
            while (i+length) in numSet:
                length +=1
            longest = max(length,longest)
    return longest

nums=[100,4,200,1,2,3]
print(longest_consecutive_seq(nums))

#Ans=[1,2,3,4] = 4