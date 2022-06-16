def majorityElement(list):
    hm={}
    res,maxCount=0,0

    for i in list:
        hm[i] = 1+hm.get(i,0)
        res=i if hm[i] > maxCount else res
        maxCount = max(hm[i],maxCount)

list=[2,2,1,1,1,2,2]
ans=majorityElement(list)
print(ans)