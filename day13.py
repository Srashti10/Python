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

# Capitalize() method is used to change the first letter of the sentence.
# It also converts all the other letters except for first to the lowercase.
blogHeading = "introduction to pyTHon"
print(blogHeading.capitalize())

# center() method is used to align the content to the center. 
# We need to give the parameter to how much unit we want to shift from the corner.
str1 = "Welcome to the console"
print(str1.center(50))  # It will make the length of the string 50.
print(len(str1))
print(len(str1.center(50)))

# count() method is used to count how many times any character occurs in the string.
print(a.count("Harry"))
name = "Harry"
print(name.count("r"))

# endswith() method is used to check whether a given string ends with a particular character or not.

