#create parent class
class mom:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def gender(self):
        print(self.name, self.age)

#create child class
class daughter(mom):
    def son(self):
        print("This is child class...")

#create object of parent
m1 = mom("Mamta", 34)
m1.gender()

#create object of child
d1 = daughter("Neha")
