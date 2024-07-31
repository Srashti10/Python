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

# title method is to capitalize first letter of each word in a sentence.
str = "He's name is Dan. Dan is an honest man."
print(str)
print(str.title())

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
# It will return a True or a False.
print(name.endswith("ry"))
print(name.endswith("y"))
print(name.endswith("h"))
# It can also checks whether a specific part of the string is ending with a the given character or not.
str1 = " Welcome to console "  # We can over write a variable in python.
print(str1.endswith("to",4,10)) # It will check whether the characters from index 4 to 9 endswith to or not.
# startswith() works same as endswith(). It will detect starting character of the string.

# find() method is used to find the first occorence of any given value.
# If the value is not present in the string then it will return -1.
print(name.find("a"))
print(name.find("r"))
print(name.find("s"))

# index method is very similar to find() method.
# but if the value is not present in the string then it will throw an error, while find() will return -1
print(name.index("r"))
#print(name.index("s"))  # It will show error because s is not present in the name string.

# isalnum() methods is used to find whether our string contains only alpha-numeric characters or not.
# It will return True if string contains only alpha-numeric charactres.(A-Z, a-z,0-9)
# If there is any other character present then it will return False.
str2 = "Srashti1"
print(str2.isalnum())
str3 = "Srashti@1"
print(str3.isalnum())

# isalpha() works same as isalnum(), but it will only detect alphabets not numeric characters. (A-Z, a-z)
str4 = "Srashti"
print(str4.isalpha())
str5 = "Srashti1"
print(str5.isalpha())

# islower() returns True if all the characters of the string are in lower case, and if not then it will return False.
# isupper() works same as islower() for the uppercase characters.
str6 = "srashti"
str7 = "Srashti"
print(str6.islower())
print(str7.islower())
print(str7.isupper())  # It will return False because all the characters of the str7 is not in uppercase.

# isprintable() returs true if all the values within the given string is printable otherwise return false.
# non printable characers are like /n (which is used for new line.)
str8 = "My name is \n Srashti"
print(str8)
print(str8.isprintable())  # Return false because \n is not printable character.

# isspace() returns True if string only contains spaces(whether it is from space bar or tab), otherwise return False.
str9 = "    "
str10 = "HelloWorld"
print(str9.isspace())
print(str10.isspace())

# istitle return true if first letter of the each word in the string is in uppercase, otherwise it will return False.
str11 = "Hey! I am Srashti Srivastava"
str12 = "Hey! I Am Srashti Srivastava"
print(str11.istitle())
print(str12.istitle())

#swapcase() method is used to swap lowercase alphabets to the uppercase and vice-versa.
str13 = "SrahtI"
print(str13.swapcase())

print(str)
print(str.title())



