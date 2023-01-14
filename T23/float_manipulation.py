# Importing math module
import math
# Importing statistics to use it's median module
import statistics

# Creating float list
float_list = []

count = 0

while count < 10:
    if count == 0:
        print("\nYou will now be asked to input numbers 10 times.\n")
    user_number = float(input("Type in a whole number or a decimal:  "))
    float_list.append(user_number)
    count += 1

print(f'''\nThe total of the numbers you inputted is:\t\t {math.fsum(float_list)}''') #Using math's sum
print(f'''The max value of the numbers you inputted is:\t\t {max(float_list)}''')
print(f'''The min value of the numbers you inputted is:\t\t {min(float_list)}''')
print(f'''The average of the values you have inputted is:\t\t {round(sum(float_list) / len(float_list), 2)} ''')
print(f'''The median number of the values you inputted is:\t {statistics.median(float_list)}''')