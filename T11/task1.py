#Setting up the variables
num1 = 101
num2 = 10
num3 = 9

#Comparing num1 and num2
if num1 > num2:
    print(f"The largest number is num1({num1}).")
elif num1 == num2:
    print(f"num1({num1}) and num2({num2}) are the same.")
else:
    print(f"The largest number is num2({num2}).")

#Checking if num1 is odd or even
if (num1 % 2) == 0:
    print(f"{num1} is an even number.")
else:
    print(f"{num1} is an odd number.")

#Sorting the numbers
larger = max(num1, num2, num3)
smaller = min(num1, num2, num3)

if(num1 > smaller and num1 < larger):
    middle = num1
elif (num2 > smaller and num2 < larger):
    middle = num2
else:
    middle = num3

#Printing the sorted number

print(f"""

The list of numbers is:

num1: {num1}
num2: {num2}
num3: {num3}

Sorted descending they look like:

{larger} > {middle} > {smaller}

""")