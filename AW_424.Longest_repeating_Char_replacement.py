def Longest_repeating_Char_replacement(s,k):
    count={}
    res=0

    l=0
    maxf=0

    for r in range(len(s)):
        print("-----------")
        print("l = ",l)
        print("s[l] = ",s[l])
        print("r = ",r)
        print("s[r] = ",s[r])
        count[s[r]]=1+count.get(s[r],0)
        print("count[s[r]] = ",count[s[r]])
        maxf=max(maxf,count[s[r]])
        print("r-l+1 = ",r-l+1)
        print("maxf = ",maxf)
        print("k = ",k)
        while (r-l+1) - maxf >k:
            count[s[l]] -=1
            print("count[s[l]] === ",count[s[l]])
            l+=1

        res=max(res,r-l+1)
    return res

s="ABAB"
k=2
print(Longest_repeating_Char_replacement(s,k))