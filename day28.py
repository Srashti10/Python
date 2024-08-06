# f-strings
# f-string is used to solve string formatting problem
letter = 'Hey! My name is {0} and I am from {1}'
name = "Srashti"
country = "India"
print(letter.format(name, country))  # name is at 0 , country is at 1.
# It will print Hey My name is Srashti and I am from India.

# Other approach for doing above is f-string
# With f-string we can directly put variables inside the string.
print(f"Hey my name is {name} and I am from {country}.")