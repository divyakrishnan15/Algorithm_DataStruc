def missingNumber(list):
    res=len(list)


    for i in range(res):
        res =res+ (i-list[i])
    return res

list=[0,3,1,2,4,6,7]

print(missingNumber(list))