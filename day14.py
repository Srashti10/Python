# If else statements
# Conditional operators:
# >, <, >=, <=, ==, !=
a = int(input("Enter your age: \n"))
if(a>18):
    print("You can drive")
else:
    print("You can not drive.")


applePrice = 210
budget = 200
if(applePrice == budget):
    print("Alexa, add apples to the cart.")
else:
    print("Alexa, do not add apples to the cart.")


# elif statement
num = int(input("Enter a number:\n"))
if(num < 0):
    print("Number is negative.")
elif(num == 0):
    print("Number is zero.")
elif(num == 999):
    print("Number is special.")
else:
    print("Number is positive.")


# nested if-else
num1 = int(input("Enter a number: \n"))
if(num1<0):
    print("Number is negative.")
elif(num1>0):
    if(num1<=10):
        print("Number is between 1 to 10.")
    elif(num1>10 and num1<=20):
        print("Number is between 11 to 20.")
    else:
        print("Number is greater than 20.")
else:
    print("Number is zero.")