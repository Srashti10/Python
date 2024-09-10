# List
# List is the ordered collection of data types.List items are seperated by commas and enclosed in brackets.
# Lists are changable, we can change them after creation.
# List can have multiple data types in the same list.
list = [1,2,'Srashti',True,[4,5],6,7,67,32,99,350]
print(list)
print(list[:])   # It will also print the entire list.
print(list[1:])  # It will print the list from index 1 to the end.
# Jump Index 
# We can print list items by jumping to some indexes.
print(list[1:11:2])  # It will print items after jumping 2 index positions.
#Since slicing indexes are 1 to 11 then it will print index elements of 1 to 10 with the gap of 2 indexes between each element.
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

#List Comprehension
#List comprehension is used for creating new lists from iterables like lists, tuples, dictionaries, sets and even in strings.

lst = [i for i in range(4)]  # It will make a list starting from number 0 to 3
lst1 = [i*i for i in range (10)]
print(lst)
print(lst1)
# We can also use conditions in list comprehension
lst2 = [i*i for i in range(10) if i%2 ==0] # It will print the number only if number is even.
print(lst2)

