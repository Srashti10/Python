# Right angle triangle pattern with stars

num = int(input('Enter the number of rows:'))
for i in range(1,num+1):   
    for j in range(1,i+1):
        print('*',end=' ')
    print()   #It will print the new line

# num1 = int(input('Enter the number:'))
# for i in range(1,num1+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()