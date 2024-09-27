# list = [1,1,3,4,4,7,8,9]
# temp = set(list)
# print(temp)

list = [1,1,6,6,6,2,2,2,5,3,3]
list.sort()
print(list)
n = len(list)

for i in list:
    if list[i] == list[i+1]:
        list.remove(list[i+1])

print(list)