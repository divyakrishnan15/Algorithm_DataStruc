def threeSum(nums):
    res=[]
    nums.sort()

    for i,n in enumerate(nums):
        print("-------------")
        print("i = ",i)
        print("n = ",n)
        print("nums[i-1] = ",nums[i-1])
        if i > 0 and n==nums[i-1]:
            continue
        l,r=0,len(nums)-1

        while l<r:
            print("l = ",l)
            print("nums[l] = ",nums[l])
            print("r = ",r)
            print("nums[r] = ",nums[r])
            threesum=n+nums[l]+nums[r]
            print("threesum = ",threesum)
            if threesum > 0:
                r-=1
            elif threesum < 0:
                l+=1
            else:
                res.append([n,nums[l],nums[r]])
                l+=1
                while nums[l]==nums[l-1] and l<r:
                    l+=1
    return res

nums=[-1,0,1,2,-1,-4]
print(threeSum(nums))