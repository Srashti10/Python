# String Slicing
names = "Srashti, Shreoshi"
print(names[0:7])   # It will print character of index 0 to index 6.(It will include index 0 but not 7)
print(names[:7])    # It will also print character of index 0 to index 6.
print(names[1:7])   # It will print character from index 1 to index 6.
print(names[:])     # It will print the character from the starting to the length of the string.
print(names[0:-3])  # It will automatically print (names[0:len(names)-3]). Which means it will print character from 0 to (17-3)
print(names[-1:-3]) # It will take len(names) before -3 and -1. In this case it will print indexes from (17-1) to (17-3)

# To find the length of any string we will use len() function
print(len(names))
fruit = "mango"
len1 = len(fruit)
print(fruit ,"is a", len1, "letter world." )