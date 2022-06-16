def mincost_climbingStairs(list):
    list.append(0)

    for i in range(len(list)-3,-1,-1):
        list[i] += min(list[i+1],list[i+2])

    return min(list[0],list[1])

list=[1,100,1,1,1,100,1,1,100,1]
res=mincost_climbingStairs(list)
print(list)