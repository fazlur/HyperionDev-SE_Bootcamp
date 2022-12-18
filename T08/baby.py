#Importing the datetime module  to get the current year
import datetime
current_year = datetime.datetime.now().year


#Getting the user birthdate and casting to an integer to be able to do calculations
birth_year = int(input("What year were you born: "))


#Checking is the difference between the birth and current year to check the age
if (current_year - birth_year) >= 18:
    print("Congrats you are old enough.")