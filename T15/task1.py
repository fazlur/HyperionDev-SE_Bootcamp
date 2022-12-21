#Calculatin the times table up to 12 of any number input by the user
user_number = int(input("Please input the number you want to calculate the times table for: ")) 

for i in range(1, 13):
    print(f"{user_number} x {i}  = {user_number * i}")