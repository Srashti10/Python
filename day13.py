# String Methods
# Strings are immutable(Can't change the string in-place. We can make a new copy of the string)
a = "!!Harry!!*!!John!!*!!Harry!!"
print(len(a))
# To convert string in uppercase upper() function is used.
print(a.upper())   # It does not change the existing string but it will create a new string with uppercase letters.
# To convert string in lowercase lower() function is used.
print(a.lower())
# To remove or strip any special character from the end of the string rstrip method is used.
# (Not remove the character if it is in the beggining of the string)
print(a.rstrip("#"))
# To replace any specific pattern inside the string with the other replace() function is used.
# It will replace harry with john , does not matter how many times it is present in the string.
print(a.replace("Harry", "John")) 
# Split() method is used to convert the string in to list.
# It will split the character of the string wherever * is present and each split term is the element of the new list.
print(a.split("*"))




