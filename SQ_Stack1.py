class Stack:
    def __init__(self):
        self.items=[]

    #def isEmpty(Self):
    #    return not self.items

    def pop(self):
        return self.items.pop()

    def push(self,item):
        self.items.append(item) 

    def peek(self):
        return self.items[-1]

    #def __str__(Self):
    #    return str(self.items)

if __name__ == "__main__":
    s=Stack()
    print(s)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    print(s)
    s.pop()
    print(s)
    s.peek()
    print(s)

