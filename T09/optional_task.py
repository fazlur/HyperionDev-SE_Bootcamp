#Checking the user role
employee_role = int(input("Type 1 if you are a manager or 2 if you are a salesperson: "))

#Getting the number of hours worked if manager or gross sales if salesperson and calculating salary based on that
if(employee_role == 1):
    hours_worked = float(input("How many hours you worked in the month: "))
    print(f"As a manger you are paid R40.00 per hour as you worked {hours_worked}, your total pay will be R{hours_worked * 40}")
elif(employee_role == 2):
    gross_sale=float(input("What was the total of your gross sales: "))
    salary = 2000
    #Calculating 8 percent of gross sales
    commission = (8 / 100) * gross_sale
    print(f"Your total compensation is R{salary} plus the sales commission R{commission} totaling at R{salary + commission}")
else:
    print("You didn't pick a valid employee role.")