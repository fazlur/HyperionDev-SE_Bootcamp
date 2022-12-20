# Creating student counter and initial message
count = 0
print("You will now be asked to type in the names of all pupils in class, type STOP once you have no more names to enter.")

# Getting user names util stop is entered
while True:            
    name = input("Student Name: ")

    if name.lower() == "stop":
        break

    count += 1

# Printing out student count
print(f"There are {count} students in class.")
