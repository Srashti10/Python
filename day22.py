# List
# List is the ordered collection of data types.List items are seperated by commas and enclosed in brackets.
# Lists are changable, we can change them after creation.
# List can have multiple data types in the same list.
list = [1,2,'Srashti',True,[4,5]]
print(list)
l = [3,5,6]
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[2])

# Negative Indexing
print(list[-3])
# To convert it in positive indexing, we can:
print(list[len(list)-3])

# We can check whwther a particular element is present in list or not
if 7 in list:
    print('Yes it is present.')
else:
    print('No, it is not present.')

# Same thing apply in string also
if "arry" in "Harry":
    print("True")
else:
    print("False")