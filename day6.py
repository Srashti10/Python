# Variables and Data Types

"""
Variables are like containers which store data,
just like there are containers in our kitchen which 
is used to store different things such as salt, sugar etc.  
"""
a = 1234567  # a is a variable which stores integer data type.
b = "Harry"  # b is a variable which stores string data type.
c= True # c is a variable which stores boolean data type.
d= None # d is a variable which stores none data type.

print(a)
print(b)
print(c)
print(d)


# type() function is used to get the data type of variable.
print("The type of a is", type(a))
print("The type of b is", type(b))
print("The type of b is", type(c))
print("The type of b is", type(d))

# Numeric Data Type

int = 897
float = 98.456
com = complex(8,2)
print(int)
print(float)
print(com)


# String Data Type


str =  "Hello World"
print(str)

# Boolean Data Type

"""
True, False
"""

# Sequence Data Type

List = [1,2,3,"Harry", True, None, ["Apple", 3, 4]]  # Mutable
Tuple = (1,3,4,("Apple","Mango"))  #Immutable
print(List)
print(Tuple)

# Mapped Data Type (Key-Value Pairs)

Dict = {"name": "Srashti", "age": 22, "canVote": True}
print(Dict)

# In Python everything is an object.
