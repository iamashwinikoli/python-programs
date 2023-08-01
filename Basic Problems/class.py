class student:                  #creating class
        age = 15
        grade = 'good' 
        name = "ashwini"
        if age<=18:
            print("sorry you are not adult")
        else:
            print("try again")
        
s1 = student                    #creating object is s1 of class student
print("Becouse Your age :", s1.age)
print("Your name is :" , s1.name)
print("Your grade is :", s1.grade)
