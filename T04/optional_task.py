#Getting input from user
num1 = int(input("Type a number : "))
num2 = int(input("Type another number : "))

#Printing the original values of num1 and num2
print(f"The original value of num1 is {num1} and the orginal value of num2 is {num2}")

#Swaping the values of the variables with single line multi variable assignement 
num1 , num2 = num2 , num1

#Printing the values of the variables after swap
print(f"The value of num1 after the swap is {num1} and value of num2 now is {num2}")