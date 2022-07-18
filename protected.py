class Base:
    def __init__(self):
        self._a=2
        print(self._a)

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("hi")

        self._a=3
        print("call protected var"+self._a)

d=Derived()
b=Base()



