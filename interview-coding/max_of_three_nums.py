def maximum(a,b,c):
    if a>b and a>c:
        return f'{a} is maximum.'
    elif b>a and b>c:
        return f"{b} is maximum."
    elif c>a and c>b:
        return f"{c} is maximum."
    
a = int(input('Enter first number'))
b = int(input('Enter second number'))
c = int(input('Enter third number'))

print(maximum(a,b,c))
