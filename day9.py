# Type Casting
# Type Casting means conversion of one data type to other data type(e.g: String to Integer)
# Two Types of Type Casting: Implicit and Explicit
"""Implicit Conversion: Python itself does the conversion without any user command.
   There are an order in data types in python. So when we are performing operations on a high order data type and 
   a low order data type, then pythin wil convert low order data type to high order data type.
"""
"""Explicit Conversion: User tells python interpreter to convert the data types.
   Various functions for explicit conversion are:
   int(), float(),hex(),oct(),str(),etc
"""

# Concatination of strings
a = "Srashti"
b = "Srivastava"
print(a+b)

# Explicit TypeCasting

c= "1"
d= "2"
print(c+d)
print(int(c) + int(d))  # converting string to integer

# for conversion it must be valid or convertible data types

c = "1SRASHTI"
d = "4"
# print(int(c) + int(d))  (It will show error because it is not possible to convert 1SRASHTI to integer.)

e = 1
f = 2
print(str(e) + str(f))  # conversion of integer to string

# Implicit TypeCasting
g = 1.9
h = 8
print(g+h)  # Python converts h from integer to float. Float has higher order than int.
print(type(g))
print(type(h))
# print(type(g+h))