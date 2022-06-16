def moveZeros(list):
    l,r=0,0

    for i in list:
        if list[r]:
            list[l],list[r]=list[r],list[l]
            l += 1
    return list

list = [0,1,0,3,12]
res=moveZeros(list)
print(res)