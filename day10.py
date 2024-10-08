# User Input
# In python we can take user input directly by using input() function

a = input()
print("My name is", a)

a = input("Enter your name:")
print("My name is", a)

x = input("Enter first number:")
y = input("Enter second number:")
print(x+y)
print(int(x) + int(y))

# input function will always consider your input as string by default
# for taking integer as input we will have to use type casting using int() function

x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
print(x+y)



# Home work
x = input("Enter first number: \n")
y = input("Enter second number: \n")

# # Other than x+y, every other operation will show error, because python consuder inputs as string 

print("The value of", x, "+" ,y, "is", x+y)
print("The value of", x, "-" ,y, "is", x-y)
print("The value of", x, "*" ,y, "is", x*y)
print("The value of", x, "/" ,y, "is", x/y)
print("The value of", x, "**" ,y, "is", x**y)
print("The value of", x, "//" ,y, "is", x//y)


x = int(input("Enter first number: \n"))
y = int(input("Enter second number: \n"))

print("The value of", x, "+" ,y, "is", x+y)
print("The value of", x, "-" ,y, "is", x-y)
print("The value of", x, "*" ,y, "is", x*y)
print("The value of", x, "/" ,y, "is", x/y)
print("The value of", x, "**" ,y, "is", x**y)
print("The value of", x, "//" ,y, "is", x//y)



