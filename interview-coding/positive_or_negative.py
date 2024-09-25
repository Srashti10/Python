def pos_or_neg(num):
    if num>0:
        return "Positive"
    elif num<0:
        return "Negative"
    else: 
        return "Zero"

num = int(input('Enter the number: '))
print(pos_or_neg(num))
