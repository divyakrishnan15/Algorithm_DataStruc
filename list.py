def list():
    list = []

    list.append(1)
    list.append(2)
    list.append(3)
    list.append(4)
    list.append(5)
    print(list)


    for i in range(len(list)):
        list.append(i)
    print(list)

    list2=["Div","US"]
    list.append(list2)
    print(list)

    list.extend("A")
    print(list)

    list.insert(0,"Z")
    print(list)
    
    a=[x for x in range(len(list)) if x%2==0]
    print(a)

    return list

if __name__ =="__main__":
    list()
    


