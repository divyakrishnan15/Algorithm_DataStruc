from os import truncate


def isAnagram(s,t):
    if len(s)!=len(t):
        return False
    
    countS,countT = {},{}

    for i in range(len(s)):
        print("--------------")
        print("i = ",i)
        countS[s[i]] = 1+countS.get(s[i],0)
        countT[t[i]] = 1+countT.get(t[i],0)
        print("countS = ",countS)
        print("countS[s[i]] = ",countS[s[i]])
        print("countT = ",countT)
        print("countT[t[i]] = ",countT[t[i]])

    for j in countS:
        print("j = ",j)
        print("countS[j] =",countS[j])
        print("countT.get(j,0) =",countT.get(j,0))
        if countS[j] != countT.get(j,0):

            return False
    return True

s=['a','n','a','g','r','a','m']
t=['n','a','g','a','r','a','m']

res=isAnagram(s,t)
print(res)