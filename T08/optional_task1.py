#Getting the user input and casting it to int
user_int = int(input("Type a number: "))

#Checking if the user picked by the user is divisible by 2 with no remainder(even)
if(user_int % 2 == 0):
    print(f"The number {user_int} is an even number.")
else:
    print(f"The number {user_int} is odd.")