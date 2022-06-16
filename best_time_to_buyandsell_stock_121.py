def maxProfit(list):
    l,r=0,1
    maxP=0

    while r < len(list):
        if list[l] < list [r]:
            profit=list[r]-list[l]
            maxP=max(maxP,profit)
        else:
            l=r
        r +=1

    return maxP

list=[7,1,5,3,6,4]
res=maxProfit(list)
print(res)

#O/P = 5