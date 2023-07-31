global_var="hello"

def mylocal():
    localVar="world"
    print("heyyy " , localVar)
    print(global_var)

mylocal()
print("hey..." , global_var)