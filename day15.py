# Exercise 2  (Good Morning Sir!)
# We have to make a program to greet a person according to the time.
# My solution

import time   # This function is used to use time in the program
timestamp = time.strftime("%H,%M,%S")  #strftime stands for string format time, It is used to display time in string format.
print(timestamp)
timestamp = int(time.strftime("%H"))
print(timestamp)
if(timestamp >= 7 and timestamp<12 ):
    print("Good Morning Sir!!")
elif(timestamp >=12 and timestamp<17):
    print("Good Afternoon Sir!!")
elif(timestamp >=16 and timestamp<22):
    print("Good Evening Sir!!")
elif(timestamp>=22 and timestamp<3):
    print("Good Night Sir!!")
else:
    print("It's very early in the morning, Sir!!")

