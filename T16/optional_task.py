# I have used the same code as for task 2(logic.py) with the same logical error
# but I am adding the runtime error by removing the casting in the age variable
# causing the if comparison to fail


age = input("How old are you in years: ")

if(age > 18):
    print("You are 18 or older, you are old enough!")
else:
    print("You are not old enough! You are less than 18 years old!")

# Below I have added two compilation errors, caused by invalid syntax 

number = I am a SyntaxWarning # A string should be wrapped in quotes
Print (number) # print should be lowercase 