# Program that checks which years are leap years whithin a range defined by the user
start_year = int(input("What year you'd like to start with? "))
years_to_check = int(input("How many years you want to checks? "))

for year in range(start_year, (start_year + years_to_check + 1)):
    #formula to calculate if year is leap
    if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
        print(f"{year} is a leap year")
    else:
        print(f"{year} isn't a leap year")