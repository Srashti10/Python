# Function Arguments
# There are four types of arguments that we can provide in a function:
# 1-Default Arguments, 2-Keyword Arguments 3-Variable length Argument 4-Required Arguments

# def average(a,b):
#     print("The average is", (a+b)/2)

# average(4,6)

# Default Arguments
def average(a=9, b=1):
    print("The average is", (a+b)/2)
average()  #Here we don't have to give arguments, because we already give the value of the arguments at the time of defining.
average(1,5) # If we give some other value which is not mentioned before,
# then it will ignore the before mentionrd value and take the current values as the argument.
# If we want to give value of a and we want to use the value of b as mentioned before, then:
average(5)  # It will give the average of 5 and 1
# If we want to give value of b and we want to use the value of a as mentioned before, then:
average(b=6)  # It will give the average of 9 and 6.

def name(fname="Amy",mname= "Farah",lname="Fowhler"):
    print("Hello",fname,mname,lname)
name()
name("Penny")
name("Penny","Bernedette")
name("Penny", "Bernedette", "Emily")

# Keyword Arguments
# We can give argument in the function like key = value, this way we don't have to think about the order of the arguments.
def addition(a,b):
    print("Addition is", a+b)
addition(b=10,a=5)

# Required Arguments
# We must have to give the value of the arguments while calling the function
# If the value of that variable is not given while declaring the function.
def gMean(a,b=10):
    print("Geometrical mean is",(a*b)/(a+b))
gMean(40) # Here it is required to give the value of a because the value is not given before.


# Variable length arguments
# Sometimes when we want to find average, mean ,sum then there can be multiple numbers of arguments.
# In this case we can give variable length of the argument, then while calling the function we can give multiple arguments.
def average(*numbers):    # Here we can give multiple number of arguments by adding * before argument(*numbers)
    sum = 0               # It will take numbers as tuple.
    for i in numbers:
        sum = sum+i
    print("Average is", sum/len(numbers))
average(5,6,7)
average(12,13,14)

# If we want to give argument as an dictionary then we can use double stars
def name(**name):   # take name as dictionary
    print("Hello",name["fname"],name["mname"],name["lname"])

name(fname="Amy",mname="Farah",lname="Fowhler")


# We can also use return to get the value in the function, and then can print it while calling it.
def mean(*numbers):
    sum = 0
    for i in numbers:
        sum = sum+i
    return sum/len(numbers)

mean = mean(10,20)
print(mean)

#If we give more than one return in the function then it will only consider the first return statement and ignore all others.
