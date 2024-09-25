def num_range(num):
    # range = 10 to 50
    if num>=10 and num<=50:
        return "Number is in range"
    else:
        return "Number is not in range"
    
num = int(input('Enter a number: \n'))
print(num_range(num))