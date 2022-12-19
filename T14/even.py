#Getting the user input
number = int(input("Type a number: "))

count = 0 # To hold the even number increments while trying to reach the user input

while count <= number:
    count += 2
    if count > number:
        break
    print(count)