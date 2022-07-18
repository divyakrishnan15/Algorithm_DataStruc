def three_sum_closest(nums,target):
    nums.sort()
    res=sum(nums[:3])


    for i in range(len(nums)-2):
        s=i+1
        e=len(nums)-1

        while s<e:
            sumhere=nums[i]+nums[s]+nums[e]
            if abs(sumhere-target)<abs(res-target):
                res=sumhere
            if sumhere<target:
                s+=1
            else:

                e-=1
    return res

nums=[-1,2,1,-4]
target=1
print(three_sum_closest(nums,target))

#Ans = 2 (-4,-1,1,2)