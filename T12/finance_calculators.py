#########################################################
#   CAPSTONE PROJECT I                                  #
#   Write a investment interest as well as home loan    #
#   repayment calculator                                #
#########################################################    

import math

# Variable to hold the bond repayment formula and its legend
# to be used when displaying the info to the user later in the code
bond_repayment_formula = """
The amount that a person will have to be repaid on a home loan each
month is calculated as follows: repayment = x = (i.P)/(1 - (1+i)^(-n))

In the formula above:
	● `P` is the present value of the house.
	● `i` is the monthly interest rate, calculated by dividing the annual
	interest rate by 12.
	● `n` is the number of months over which the bond will be repaid.
"""

# Variable to hold text to be displayed to user if simple interest is chosen
# as the investment product later in the code
simple_formula = """
The total amount when simple interest is applied is calculated as
follows: A = P(1 + r * t)
"""

# Variable to hold text to be displayed to user if simple interest is chosen
# as the investment product later in the code
compound_formula = """
The total amount when compound interest is applied is calculated as
follows: A = P(1 + r) ^ t
"""

# Variable to hold text to be used when outputting the legend of the interest formula 
# to the user when processing an investment simulation later in the code
investment_formula_legend = """
In the formulae above:
    ● `r` is the interest
    ● `P` is the deposit amount
    ● `t` is the number of years that the money is being invested.
    ● `A` is the total amount once the interest has been applied.
"""

###  Program Processing and Execution ###


# Getting the user to choose if they want to use the calculator for investments or bonds
while True:
    investment_type = input("""

=======================================================================
|Choose either 'investment' or 'bond' from the menu below to proceed: |
=======================================================================

investment  - to calculate the amount of interest you'll earn on your investment
bond        - to calculate the amount you will have to pay in a home loan

Type your choice here: """)

    if investment_type.lower() == "investment":
        investment = True #Boolean to hold True in case of investment or False in case of bond
        break
    elif investment_type.lower() == "bond":
        investment = False
        break
    else:
        print("""

You chose an invalid option, make sure that you type in 'investment' or 'bond' in your choice  
----------------------------------------------------------------------------------------------
""")

# Process investment information and provide calculation results
if investment:
    print("""
Your choice was investment, provide the following information:
    """)
    # Gathering required information for interest calculations
    deposit_amount = float(input("How much money are you investing: "))
    interest_rate = float(input("What is the expected interest rate percentage: "))
    years_investing = int(input("For how long you want to invest in years: "))

    #Checking for interest type, and making sure the user picks a valid option
    while True:
        interest = input("""
Type in 'simple' or 'compound' to choose the interest type: """)
        if(interest.lower() == "simple" or interest.lower() == "compound"):
            break
        # Repeating the question due to invalid response
        else:
            print("""
You chose an invalid option, make sure that you type in 'simple' or 'compound' in your choice  
----------------------------------------------------------------------------------------------
            """)

     # Processing simple interest
    if (interest.lower() == "simple"):
        print(f"""
Simple Interest Formula:
-----------------------
{simple_formula}
{investment_formula_legend}

Simple Interest Calculation:
---------------------------
Deposit Amount:     R{deposit_amount}
Interest Rate:      {interest_rate}%
Years Investing:    {years_investing}

Total Return:       R{round(deposit_amount * (1 + (interest_rate / 100) * years_investing), 2)} """)

    # Processing compound interest
    else:
        print(f"""
Compound Interest Formula:
--------------------------
{compound_formula}
{investment_formula_legend}

Compound Interest Calculation:
------------------------------
Deposit Amount:     R{deposit_amount}
Interest Rate:      {interest_rate}%
Years Investing:    {years_investing}

Total Return:       R{round(deposit_amount * math.pow((1 + (interest_rate / 100)), years_investing), 2)} """)

# Process bond information and provide calculation results
else:
    print("Your choice was bond, provide the following information: ")
    house_value = float(input("What is the value of the house: "))
    interest_rate = float(input("What is the annual interest rate percentage: "))
    months_repaying = int(input("How many repayment months: "))
    #Calculating the value of i (interest rate divided by 12)
    i = (interest_rate / 100) / 12
    print(f"""
Bond Repayment Formula:
-----------------------
{bond_repayment_formula}

Bond Repayment Calculation:
--------------------------

House Value:        R{round(house_value, 2)}
Annual Interest:    {round(interest_rate)}%
Months Repaying:    {months_repaying}

Monthly Repayments: R{round((i * house_value) / (1 - (1 + i) ** (-months_repaying)),2)} """)