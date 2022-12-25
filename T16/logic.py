# In the program below we want to check if someone is old enough to buy beer
# 18+ years, but I am using a comparison operator that does not include people
# that have just turned 18, allowing the program to run but with a logical error

age = int(input("How old are you in years: "))

if(age > 18):
    print("You are 18 or older, you are old enough!")
else:
    print("You are not old enough! You are less than 18 years old!")