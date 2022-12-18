#Asking the user for 3 numbers and storing them as int
int_1 = int(input("Pick your first number: "))
int_2 = int(input("Pick your second number: "))
int_3 = int(input("Pick your third number: "))

#Using the f in the print to convert the result of the sum of the 3 numbers into a string for printing
print(f"The sum of all the numbers you chose is: {int_1 + int_2 + int_3}")

#Subtracting the 1st number by the second
print(f"Subtracting the first number ({int_1}) by the second ({int_2}) = {int_1 - int_2}")

#Multiplying the 3rd number by the 1st
print(f"Multiplying the third number ({int_3}) by the first ({int_1}) = {int_3 * int_1}")

#Summing all the numbers then dividing the result by the third
print(f"The sum of all three numbers is ({int_1 + int_2 + int_3}) if we divide that by the third number ({int_3}) = {(int_1 + int_2 + int_3) / int_3}")
