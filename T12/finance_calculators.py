"""
CAPSTONE PROJECT I
Write a investment interest as well as home loan
repayment calculator
"""

import math

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
formula_legend = """
In the formulae above:
    ● `r` is the interest
    ● `P` is the deposit amount
    ● `t` is the number of years that the money is being invested.
    ● `A` is the total amount once the interest has been applied.
"""

###  Program Processing and Execution ###


# Getting the user to choose if they want to use the calculator for investment or bond
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
Your choice is not valid!
            """)

    if (interest.lower() == "simple"):
        print(f"""
Simple Interest formula:
-----------------------
{simple_formula}
{formula_legend}

Based on the values you have entered the total amount that you will have if you
invest R{deposit_amount}, over {years_investing} years, at {interest_rate}%
is: R{round(deposit_amount * (1 + (interest_rate / 100) * years_investing), 2)}

        """)
    # Processing compound interest
    else:
        print(f"""
Compound Interest formula:
-------------------------
{compound_formula}
{formula_legend}

Based on the values you have entered the total amount that you will have if you
invest R{deposit_amount}, over {years_investing} years, at {interest_rate}%
is: R{round(deposit_amount * math.pow((1 + (interest_rate / 100)), years_investing), 2)}
        """)
# Process bond information and provide calculation results
else:
    print(f"You chose {investment}")