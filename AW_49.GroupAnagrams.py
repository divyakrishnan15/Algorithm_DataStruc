import collections
def GroupAnagrams(strs):
    ans = collections.defaultdict(list)
        
    for s in strs:
        print("-----------")
        print("s = ",s)
        count = [0] * 26
        print("count = ",count)
        for c in s:
            print("c = ",c)
            print("ord(c) = ",ord(c))
            print("ord('a') = ",ord('a'))
            print("count[ord(c) - ord('a')] = ",count[ord(c) - ord('a')])
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)
        print("ans = ",ans.values())
    return ans.values()

strs = ["eat","tea","tan","ate","nat","bat"]
print(GroupAnagrams(strs))
