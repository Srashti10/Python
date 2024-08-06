# Exercise2 Solution  (Good Morning Sir)
# My solution in day 15
# We have to make a program to greet a person according to the time.
# "Harry's Solution"

import time 
t = time.strftime('%H:%M:%S')
hour = int(time.strftime("%H"))
print(hour)

if(hour>=0 and hour<12):
    print("Good Morning Sir!")
elif(hour>12 and hour<17):
    print("Good Afternoon Sir")
elif(hour>=17 and hour<0):
    print("Good Night Sir")