import string
str = "ashwini koli"
print(str)
print(str[1])
print(str[2:5])
print(len(str))
print(str.upper())
print(str.lower())
print(str.replace("a", "R"))

if "hello" in str:
    print("yes this name is present in the string...")
else:
    print("sorry we can't find this name....")

if str in str:
    print(str)