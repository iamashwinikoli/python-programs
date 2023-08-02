#creat parent class
class parent :
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def inher(self):
        print(self.name, self.salary)

#creat child class 
class son(parent):
    def sum(self):
        print("This is child class")

#crete object of parent class
p1 = parent("Amar",80000)
p1.inher()

#create object of child class
son_datails = son("Arun", 50000)

#create parent class function
son_datails.inher()

#create child class function
son_datails.sum()