class Solution():
    def encode(self, strs):
        res = ""
        for s in strs:
            print("----- ENCODE -------")
            print("s = ",s)
            #res += str(len(s)) + "#" + s
            res += "#" + s
            print("res = ",res)
        return res

    def decode(self, str):
        res, i = [], 0

        while i < len(str):
            print("----- DECODE -------")
            print("i = ",i)
            print("len(str) = ",len(str))
            
            j = i
            print("j = ",j)
            print("str[j] = ",str[j])
            while str[j] != "#":
                j += 1
                print("i = ",i)
                print("j = ",j)
                print("decode j =",j)
            print("str[i:j] = ",str[i:j-1])
            length = int(str[i:j-1])
            print("str[j + 1 : j + 1 + length] = ",str[j + 1 : j + 1 + length])
            res.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res

a=Solution()
strs=["how","are","you","divya"]
print(a.encode(strs))
print(a.decode(strs))