arr = [1,2,3,5]
n = 5
sum1 = int((n*(n+1))/2)
sum2 = 0
for i in arr:
    sum2 = sum2 + i
print(sum1)
print(sum2)
m = sum1 - sum2
print(m)