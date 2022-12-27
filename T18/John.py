# Creating list to hold incorrectly guessed names
incorrect_names = []

#Loop to capture user inputted name and add it to incorrect_names list until john is typed by the user
while True:
    name = input("Enter your name: ")
    if name.lower() == "john":
        break
    else:
        incorrect_names.append(name)

#Printing out the lust populated with incorrect names
print(f"Incorrect names: {incorrect_names}")