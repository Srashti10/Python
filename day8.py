# Calculator Exercise

# My solution

num1 = int(input("Enter first number: \n"))
num2 = int(input("Enter second number: \n"))
operator = input("Enter one of the given operator (+,-,*,/,**,%,//): \n")
if (operator == "+"):
    print("Addition of given numbers is", num1+num2)
elif (operator == "-"):
    print("Subtraction of given numbers is", num1-num2)
elif (operator == "*"):
    print("Multiplication of given numbers is", num1*num2)
elif (operator == "/"):
    print("Division of given numbers is", num1/num2)
elif (operator == "**"):
    print("Exponent of given numbers is" , num1**num2)
elif (operator == "%"):
    print("Modulus of given numbers is", num1%num2)
elif (operator == "//"):
    print("Floor Division of given numbers is", num1//num2)


# To replicate lines (Alt+Shift+DownArrow)
# To get multiple cursors (Alt + click)

# Harry's Sulution

a = 50
b = 3

print("The value of" ,a, "+" ,b, "is:", a+b )
print("The value of" ,a, "-" ,b, "is:", a-b )
print("The value of" ,a, "*" ,b, "is:", a*b )
print("The value of" ,a, "/" ,b, "is:", a/b )


