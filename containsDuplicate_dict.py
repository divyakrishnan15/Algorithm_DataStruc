from collections import defaultdict

def containsDuplicate(nums):
    dict = defaultdict(int)

    for i in nums:
        if dict[i]:
            return True,i
        dict[i]+=1
    return False

nums=[1,2,3,4,2,1]
print(containsDuplicate(nums))
