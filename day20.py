# Functions
# If we want to repeat the logic of code multiple times in our program, we have to repeat it multiple times.
# But we don't want to repeat specific part multiple times because , because it is very difficult to update in multiple times.
# But with the help of functions we can make that portion of code a different entity anduse it multiple places in the program.
# Functions are of two types: 1- Built-in function 2- User-defined functions  
# In built-in function we don't have to use the def keyword. some examples of built-in functions are: range(), print(),type().
# Rules of naming the functions are same as variables.
# Geometric Mean = (a*b)/(a+b)
# How to create a function to create geometric mean.
def calculateGmean(a,b):    # calculateGmean = name of the function, (a,b) = arguments of the function
    mean=(a*b)/(a+b)
    print(mean)

# Create a function to check which number is greater
def isGreater(a,b):
    if(a>b):
        print("First number is greater.")
    elif(a<b):
        print("Second number is greater.")
    else:
        print("Both numbers are equal.")

# If we want to declare a function now and wanted to add function body later, then we can use pass statement to tell python
# interpreter that you will add the function body later. If you leave it without giving pass, then it will show error.
def isLesser(a,b):
    pass  # pass means go to the next line to execute


calculateGmean(10,20)    # calling of the function calculateGmean
isGreater(30,40)  # calling of the function isGreater.