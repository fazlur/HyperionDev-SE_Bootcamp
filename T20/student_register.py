# Getting the total number of students registering
while True:
    total_students = (input("How many students are registering: "))
    # Making sure that the user types in a valid number of students
    if total_students.isnumeric():
        break
    else:
        print("\nPlease type a valid number of students!\n")


# Line to sign - to be used later when writing to file
dotted_line = """
Student Signature below:


------------------------------------------------------

"""

# Casting the variable to int to use it as a counter in the next loop
total_students = int(total_students)

# Opening file for writing using with to ensure the file is closed once operations are concluded
with open('reg_form.txt', 'w') as file:
    # Looping through the total number of students, getting their ID and printing a line for their signature
    while True:
        id = (input("Type in your student ID: "))
        if id.isnumeric():
            file.write("Student ID: " + id + "\n" + dotted_line)
            total_students -= 1
        else:
            print("\nPlease type in a valid student ID!\n")

        if total_students == 0:
            break
