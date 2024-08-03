# break and continue statements
# break statement - to break and exit the loop
# continue statement - to skip a particular iteration of the loop.

for i in range(1,10):
    print(i)
    break
#The upper block of code will print 1 only. Because after print statement there is a break statement, so it will exit the loop.

# for i in range(12):
#     print("5 X",i+1,"=",5*(i+1))
#     if(i==10):
#         break
# print("Loop ko chod kar nikal gaya")


for i in range(12):
    if(i==10):
        print("Skip the iteration")
        continue
    print("5 X", i+1 ,"=", 5*(i+1))


# Emulation of do-while loop
i=0
while True:
    print(i)
    i = i=1
    if(i%100 == 0):
        break