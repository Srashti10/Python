# Tuples
# Tuple elements are enclosed inside parenthesis(). We can not change the tuple. It is immutable.
tup = (1,5,6, "Harry", True,4.56)
print(tup)
print(type(tup))

# If we give only one value inside paranthesis, then python interpreter will consider it as integer.
# If we want to create tuple with single element we should use comma(,) with it.
tup1 = (1)  # The type of this tup1 will be int.
tup2 = (1,)  # The type of this tup2 will be tuple.
print(type(tup1))
print(type(tup2))

# We can change elements in list, but not in tuple.
list = [1,2,3,4]
list[1] = 40  # It will change the first index value to 40.
print(list)

tuple = (1,2,3,4)
#tuple[1] = 40  # This will show error as tuples are immutable.
print(tuple)

# Positive and negative indexing are same as lists in tuple.
# We can convert negative indexing to positive indexing by writing len(tuple) before negative indexing
# tuple[-3] = tuple[len(tuple)-3]
print(tuple[-3])  # It will print tup[len(tuple)-3] = tup[4-3] = tup[1] = 2

# We can chech whether a particular value is present in the tuple or not
if 4 in tuple:
    print("Yes")
else:
    print("No")

# Slicing is also possible in tuple same as list. But it will not change the value of existing tuple.
# It will return a new tuple.

print(tuple[1:3])
print(tuple)  # The value of tuple remains same.
tuple2 = tuple[1:4]
print(tuple2)
print(tuple[0:])  # It is equal to tuple[0:len(tuple)]
print(tuple[:4])  # It is equal to tuple[0:4]
print(tuple[:])   # It will print the entire tuple.