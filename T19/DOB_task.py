# Variables to hold data from the file after splitting the lines per name and birthdate
dob_data = []
name_data = []

# Reading the file and passing it's contents to the lists that 
with open('DOB.txt', 'r') as file:
    for line in file:
        # Splitting the after the second occurrence of a space and storing everyting up to that in name_data
        name_data.append(line.split(" ", 2)[:2])
        # Stripping the carriage return from the line and then 
        # splitting it after the second occurrence of a space and storing and storing everything from onwards that point in dob_data
        dob_data.append((line.strip().split(" ", 2)[2:]))

# Printing the list containing the names
print("""
========
¦ NAME ¦
========""")
for name in name_data:
    # Using the * to unpack the list, remove the brackets, etc.
    print(*name)

print("""
==============
¦ Birthdate  ¦
==============""")
for dob in dob_data:
    # Using the * to unpack the list, remove the brackets, etc.
    print(*dob)