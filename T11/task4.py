#Getting int from user
number =  int(input("Type in a whole number to check if it is divisible by 2 and/or 5: "))

#Checking if the number is divisible by 2 and/or  5 and providing the result of the division when divisible
if(number % 2 == 0) and (number % 5 == 0):
    print(f"""
The number you have chosen ({number})  is divisible by 2 and 5
{number} / 2 = {number / 2} 
{number} / 5 = {number / 5} 
    """)
elif (number % 2 == 0) or (number % 5 == 0):
    if(number % 2 == 0):
        print(f"""
The number you picked ({number}) is not divisible by 5 but can be divided by 2:
{number} / 2 = {number / 2} 
    """)
    else:
        print(f"""
The number you picked ({number}) is not divisible by 5 but can be divided by 2:
{number} / 5 = {number / 5} 
    """)
else:
    print(f"The number {number} is not divisible by 2 or 5")