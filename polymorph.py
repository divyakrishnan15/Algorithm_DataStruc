class Bird:
    def intro(self):
        print("intro")
    
    def flight(self):
        print("birds can fly")

class Sparrow(Bird):
    def flight(self):
        print("Sparrow can fly")

class Ostrich(Bird):
    def flight(self):
        print("Ostrich CANNOT fly")

b=Bird()
s=Sparrow()
o=Ostrich()

b.intro()
b.flight()

s.intro()
s.flight()

o.intro()
o.flight()

# intro
# birds can fly
# intro
# Sparrow can fly
# intro
# Ostrich CANNOT fly