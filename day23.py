# List Methods
l = [1, 2, 34, 67, 8, 4, 6]
print(l)

# append method is used to add new element in the list.
l.append(7)  # It will add element 7 in the end of the list.
print(l)   

# sort method is used to sort the list items in increasing order.
l.sort()
print(l)

# If we want to sort list items in descending order then inside sort function we have to give (reverse = True)
l.sort(reverse= True)
print(l)

# reverse method is used to reverse the elements of the list
l1 = [10,34,76,2,68,98]
l1.reverse()
print(l1)

# index method is used to give the index value of the given element.
l2 = [87, 56, 98, 90, 90, 76, 78]
print(l2.index(76))   # Element 76 is present at index 5 so it will print 5
print(l2.index(90))   # It will print 3 because first occurence of the element 90 is at index 3.

# count method is to find how many times an element is present in the list.
l3 = [45,78,98,45,90,45,78,90]
print(l3.count(98))   # 98 is present one time in the list so it will print 1.
print(l3.count(45))   # 45 is present three times in the list so it will print 3.

# If we directly do m = l3, it will not make a new list with all the elements of l3, but it will use m as the reference of l3.
# If after doing m = l3 , we make changes in m then it will also change the element of l3.
m = l3
m[0] = 0  # It wil also change the index element of l3 to 0
print(l3)

# If we don't want want this , then we have to use copy method.
# If we use copy function then it will copy the elements of one list to other.
# And if we make the changes in new list then it will not change the existing list.
m = l3.copy() # It will copy the elements of l3 to m and if we make changes in m it will not reflect in l3.
m[0] = 50  # It only change the value of m, not l3.
print(l3)

# insert method is used to insert new element in the list at a given index.
l4 = [23, 45, 98, 56, 90, 80]
l4.insert(1,900)  # It will add element 900 at index 1 in l4.
print(l4)

m1 = [1,2,3,4,5]
m2 = [6,7,8,9,10]
m1.extend(m2)   # It will add the entire m2 list at the end of m1.
print(m1)

# If we want to concatinate m1 and m2 without changing m1 and m2 , then we can simply add it.
newM1 = [4,5,8,20]
newM2 = [78,45,90,54]
newM = newM1 + newM2
print(newM)