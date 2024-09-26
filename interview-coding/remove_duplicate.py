# list = [1,1,3,4,4,7,8,9]
# temp = set(list)
# print(temp)

list = [1,1,6,6,6,2,2,2,5,3,3]
app = list.sort()
n = len(app)
for i in app:
    if app[i] == app[i+1]:
        list.remove(app[i+1])

print(a)