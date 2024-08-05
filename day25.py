# Tuple Methods
# If we want to add, remove or change tuple then first we have to change the tuple into list,
# make changes and convert it again to a tuple.

countries = ("Spain", "Itlay", "India", "England", "Germany")   # Tuple of countries
temp = list(countries)   # It will convert the tuple of countries in a list named temp.
print (countries)
print(temp)
print(type(countries), type(temp))
temp.append("Russia")  # It will add country Russia in the temp list.
temp.pop(3)  # It will remove the element at index 3 in the temp list.
temp[2] = "Finland" # It will change the element at index 2 to Finland
countries = tuple(temp)  # It will convert the temp list into a tuple named countries.
print(countries)   # This way we can indirectly change a tuple.

# We can directly concatinate two tuples without converting it to the list.
# Becuase by concatinating we are creating a new tuple, and not making changes in the existing.
countries1 = ("Pakistan","Afghanistan","Bangladesh","SriLanka")
countries2 = ("Vietnam","India","China")
southEastAsia = countries1 + countries2  # It will create a new tuple named southEastAsia.

# count method is used to count the occurence of an element in a tuple.
tuple1 = (0,1,2,3,2,3,1,3,2,3)
print(tuple1.count(3))   # It will count the number of times 3 is present in the tuple.

# index method is used to find the first occurence of any given value.
# It will raise the value error if the element is not present in the tuple.
print(tuple1.index(3))   # Element 3 is first present at index 3 so it will return 3
# We can also check the first occurence of an element in the given portion.
print(tuple1.index(3,4,8))  # It will check first occurence of 3 from index 4 to index 8.

# len() method is used to find the length of the tuple
print(len(tuple1))



 