def email_Unique(list):
    hashset=set()

    for i in list:
        local,domain = i.split("@")
        #print(local)
        #print(domain)
        local = local.split("+")[0]
        #print("---")
        #print(local)
        local = local.replace(".","")
        #print("---")
        #print(local)
        hashset.add((local+"@"+domain))
        print(hashset)
        
    return len(hashset),hashset(2)

list = "m.y+name@email.com","alice.z@leetcode.com","test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"
res=email_Unique(list)
print(res)