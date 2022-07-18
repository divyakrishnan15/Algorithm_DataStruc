class Base:
    def __init__(self):
        self.a="Divya"
        self.__c="hi"

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("hi"+self.__c)
a=Base()
print(a)
b=Derived()
print(b)
#print(b.self.__c)

