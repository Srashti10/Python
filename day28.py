# f-strings
# f-string is used to solve string formatting problem.
# fstring is introduce in python 3.6 onwards.
letter = 'Hey! My name is {0} and I am from {1}'
name = "Srashti"
country = "India"
print(letter.format(name, country))  # name is at 0 , country is at 1.
# It will print Hey My name is Srashti and I am from India.

# Other approach for doing above is f-string
# With f-string we can directly put variables inside the string.
print(f"Hey my name is {name} and I am from {country}.")

# If we want to print the above string exact as it is written. Then we have to use double curly braces.
print(f"We use f-string like this. Hey my name is {{name}} and I am from {{country}}")

# f string can also be used to display floating number to a given range after decimal.
price = 46.0999978
txt =f" For only {price:.2f} dollars"  # by using .2f it will print till two places after decimal. 
print(txt)

# By f string we can directly directly convert an integer to a string.
print(f"{2*30}")  # It will print 60 as a string.
print(type(f"{2*30}"))

