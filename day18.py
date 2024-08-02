# While Loops
# As soon as condition becomes false python comes out of the loop
i=0
while(i<3):
    print(i)
    i = i+1
print("Loop is ended")

#
    
# Decrementing while loop

count = 5
while(count>0):
    print(count)
    count = count-1

#Infinite Loop
# count = 5
# while(count>0):
#     print(count)
#     count = count +1

# We can use else with the while loop. As soon as while loop condition becomes false it comes in the else condition.
count = 5
while(count>0):
    print(count)
    count = count-1
else:
    print("I am inside else")

# Do while loop does not work in python
# We can emulate do-while loop in python
# In do-while loop atleast, it executes at-least once irrespective of whether the condition is true or not.
# Elumination of do-while loop in python

i = int(input("Enter the number: "))
while (i<=38):
    i = int(input("Enter the number: "))
    print(i)