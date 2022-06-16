def containsDuplicate(list):
    hashset = set()

    for i in list:
        if i in hashset:
            return True,i
        hashset.add(i)
        print(hashset)
    return False

list=[1,4,5,6,4,1]
res=containsDuplicate(list)
print(res)