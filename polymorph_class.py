class India:
    def capital(self):
        print("India capital")

    def language(self):
        print("India Lang")

    def type(self):
        print("India Type")

class USA:
    def capital(self):
        print("US capital")

    def language(self):
        print("US Lang")

    def type(self):
        print("US Type")

i=India()
u=USA()

for x in (i,u):
    x.capital()
    x.language()
    x.type()

# India capital
# India Lang
# India Type
# US capital
# US Lang
# US Type