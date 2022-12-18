#Using input to take the user favorite restaurant, the variable will be set to string
fav_rest = input("Whats is your favorite restaurant: ")

#Using input to take the user favorite number but casting it to int
int_fav = int(input("What is your favorite number: "))

#Using print to print out the values of both variables in separate lines
print (fav_rest)
print(int_fav)

"""
Below is the attempt of casting a string with non numeric values to an int
the error thrown when that happens is:
    ValueError: invalid literal for int() with base 10: 'test'
this error happens because we cannot cast non numeric values to base 10 
numeric values
"""
fav_rest = int(fav_rest)