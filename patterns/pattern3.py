# # Pyramid based pattern
# num = int(input('Enter the number of rows:'))
# for i in range(0,num):
#     for i in range(0,num-i-1):
#         print(end="")
#     for i in range(0,num-i):
#         print('*',end="")
#     print()

# num = int(input('Enter the number of rows:'))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()

# num = int(input('Enter the number of rows:'))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(i,end='')
#     print()

# num = int(input('Enter the number of rows:'))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()

num = int(input('Enter the number of rows:'))
k = 1
for i in range(1,num+1):
    for j in range(1,k+1):
        print('*',end='')
    k = k+2
    print()