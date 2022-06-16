class Person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def display(self):
        print(self.name)
        print(self.id)
        print("++++++++")

    def details(self):
        print("My name is "+self.name)
        print("Id is"+self.id)
        print("----")

class Employee(Person):
    def __init__(self,name,id,sal,posi):
        self.sal=sal
        self.posi=posi

        Person.__init__(self,name,id)

    def details(self):
        print(self.name)
        print(self.id)
        print(self.sal)
        print(self.posi)

a=Employee("Divya","001","100.00","PM")

a.display()
a.details()

