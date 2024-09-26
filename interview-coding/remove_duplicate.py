# list = [1,1,3,4,4,7,8,9]
# temp = set(list)
# print(temp)

list = [1,1,6,6,6,2,2,2,5,3,3]
a = list.sort()
n = len(a)
for i in a:
    if a[i] == a[i+1]:
        list.remove(a[i+1])

print(a)