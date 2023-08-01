#creats class
class doctor:
    def __init__(self,name,occup):
        self.name = name 
        self.occup = occup
    def work(self):
        print("I am a Doctor....")

class engineer:
    def __init__(self,name,occup):
        self.name = name
        self.occup = occup
    def work(self):
        print("I am a Software Engineer....")

class teacher:
    def __init__(self,name,occup):
        self.name = name
        self.occup = occup
    def work(self):
        print("I am a Teacher.....")

class farmer:
    def __init__(self,name,occup):
        self.name = name
        self.occup = occup
    def work(self):
        print("I am a Farmer.....")
class chef:
    def __init__(self,name,occup):
        self.name = name
        self.occup = occup
    def work(self):
        print("I am a Master Chef.....")

#creats objects for all class
d1 = doctor("Amit","Doctor")
e1 = engineer("Sandeep","Software Engineer")
t1 = teacher("Pranjal", "Teacher")
f1 = farmer("Gayatri", "Farmer")

for i in (d1,e1,t1,f1):
    i.work()