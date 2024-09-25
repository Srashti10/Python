# def factorial(num):
#     if num == 0:
#         return 1
#     else:
#         return num * factorial(num-1)
    
# num = int(input('Enter the number: '))
# print(f'Factorial of {num} is ', factorial(num))

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
    
print(factorial(3))