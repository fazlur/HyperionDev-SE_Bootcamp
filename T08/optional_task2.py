#Characteristics to check, setting them all to False as default
over_20_degrees = False
weekend = False
sunny = False

#Checking if and setting the conditions based on the user response
temperature_check = input("Is the temperature higher than 20 degrees? (Answer Yes or No) :")
if (temperature_check.lower() == "yes"):
    over_20_degrees = True

weekend_check = input("Is today a weekend day? (Answer Yes or No) :")
if (weekend_check.lower() == "yes"):
    weekend = True

sunny_check = input("Is it sunny today? (Answer Yes or No) :")
if (sunny_check.lower() == "yes"):
    sunny = True

#Setting up close items depending on the value of the conditions
if(over_20_degrees):
    shirt = "short-sleeved shirt"
else:
    shirt = "long-sleeved shirt"

if(weekend):
    bottoms = "shorts"
else:
    bottoms = "jeans"

if(sunny):
    over_head = "cap"
else:
    over_head = "raincoat"

#Building a sentence based on the values of the conditions checked previously
print(f"Today you should wear a {shirt} and {bottoms} with a {over_head}")
