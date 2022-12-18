#Getting user input
full_name = input("What is your full name: ")

#Checking if variable is empty and if so flag to user to input full name
if(not full_name):
    print("You haven’t entered anything. Please enter your full name.")
#Checking if the string inputted is less tha 4 characters
elif(len(full_name) < 4):
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
#Checking if the string inputted is more than 25 characters
elif(len(full_name) > 25):
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
#Thanking the user if all previous conditions were False, we now have a full name
else:
    print("Thank you for entering your name.")