def multiplytwonumber(a,b):
    product=a*b
    if product <= 1000:
        return product
    else:
        return a+b
        

result = multiplytwonumber(20,30)
print("The product is :", result)

result = multiplytwonumber(40,30)
print("The sum of two numbers is:", result)