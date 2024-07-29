# Type Casting
# Type Casting means conversion of one data type to other data type(e.g: String to Integer)
# Two Types of Type Casting: Implicit and Explicit
# Implicit Conversion: Python itself does the conversion without any user command.
# Explicit Conversion: User tells python interpreter to convert the data types. Various functions for explicit conversion are:
# int(), float(),hex(),oct(),str(),etc

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

