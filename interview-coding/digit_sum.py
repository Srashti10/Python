# def digit_sum(num):
#     sum = 0
#     for digits in str(num):
#         sum = sum + int(digits)
#     return sum

# num = int(input('Enter the number: '))
# print(digit_sum(num))

num = int(input('Enter the number: '))
sum = 0
for digits in str(num):
    sum = sum+int(digits)
print(sum)
