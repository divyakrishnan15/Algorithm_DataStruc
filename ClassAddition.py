class Addition:
    first=0
    sec=0
    ans=0

    def __init__(self,first,sec):
        self.first=first
        self.sec=sec

    def display(self):
        print(self.first)
        print(self.sec)
        print(self.ans)

    def calculate(self):
        self.ans=self.first+self.sec

a=Addition(100,200)
a.calculate()
a.display()