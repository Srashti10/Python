# Match Case Statement
# Same as switch case statement in C/C++/Java
x = int(input("Enter the value of x: "))
# x is a variable to match
match x:
    case 0:  # If x is zero
        print("x is zero")
    case 4:  # Case with if condition
        print("x is 4")
    case _ if x!=90:
        print(x,"is not 90")
    case _ if x!= 80:
        print(x,"is not 80")
    case _:
        print(x)



   
