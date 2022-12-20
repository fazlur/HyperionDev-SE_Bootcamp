# Ask a user to input a number <= 100, continue to ask if not
# If odd multiply by 3, if even multiply by 2, in either case print the result

while True:
    user_input = int(input("Pease enter a number smaller or equal to 100: "))

    if (user_input <= 100):
        if (user_input % 2) == 0:
            print(f"The number {user_input} is even, multiplied by 2 is {user_input * 2}")
            break
        else:
            print(f"The number {user_input} is odd, multiplied by 3 is {user_input * 3}")
            break