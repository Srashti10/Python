# Functions
# If we want to repeat the logic of code multiple times in our program, we have to repeat it multiple times.
# But we don't want to repeat specific part multiple times because , because it is very difficult to update in multiple times.
# But with the help of functions we can make that ortion of code a different entity an dthen use it multiple places in the program.
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




calculateGmean(10,20)    # calling of the function calculateGmean
isGreater(30,40)  # calling of the function isGreater.