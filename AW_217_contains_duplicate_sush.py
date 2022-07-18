def abc(nums):
    list1=[]
    for i in range(0,len(nums)):
        if nums[i] not in list1:
            list1.append(nums[i])
            continue
        if nums[i] in list1:
            return True
    return False

nums=[1,2,3]
print(abc(nums))