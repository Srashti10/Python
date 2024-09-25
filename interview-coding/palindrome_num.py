num = int(input('Enter the number: '))
temp = str(num)
if temp == temp[::-1]:
    print('Number is palindrome.')
else:
    print('Number is not palindrome.')
