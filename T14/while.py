# Starting variables to later user in average calculation and initial message
count = 0
numbers = 0

print("""
Average Calculation
--------------------

Please enter the numbers you want to calculate the average on. Once you have completed entering the numbers enter -1 for the average.

""")

while True:
    user_input = int(input("Pease enter a number: "))

    if user_input == -1:
        if count <= 1:
            print(f"You have only entered one number, there is no average to calculate.")
            break

        print(f"""
The sum of the numbers you entered is:  {numbers}
These many times you entered numbers:   {count}
The average based on that is :          {numbers / count} """)
        
        break

    count += 1
    numbers += user_input