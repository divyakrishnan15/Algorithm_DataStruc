from collections import defaultdict


def dictmeth():
    dict=defaultdict(int)

    for i in range(len(l)):
        dict[i]+=i
    return

l=[1,2,3,4,1,2]
print(dictmeth(l))