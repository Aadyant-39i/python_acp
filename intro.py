x = int(input("enter a number: "))
y = int(input("enter another number: "))
z = input("what operation do you want to perform? (sum, difference, product, quotient, odd or even, remainder): ")

if z == "sum":
    result = x + y
    print("The sum is:", result)
elif z == "difference":
    result = x - y
    print("The difference is:", result)
elif z == "product":
    result = x * y
    print("The product is:" , result)
elif z == "quotient":
    if y or x == 0:
        print("Error: Division by zero is not allowed.")
    else:
       result = x / y
       print("The quotient is:", result)    
elif z == "odd or even":
    if x % 2 == 0:
        print(x, "is even.")
    else:
        print(x, "is odd.")
    if y % 2 == 0:
        print(y, "is even.")
    else:
        print(y, "is odd.")
    
elif z == "remainder":
    if y == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = x % y
        print("The remainder is:", result)
