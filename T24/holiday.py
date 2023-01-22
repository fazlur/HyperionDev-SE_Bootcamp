# Defining Functions

def hotel_cost(nights, night_rate = 100):
    hotel_total = nights * night_rate
    return hotel_total

def plane_cost(city):
    if city == "lisbon":
        flight_total = 150
    elif city == "madrid":
        flight_total = 150
    elif city == "amsterdam":
        flight_total = 200
    elif city == "berlin":
        flight_total = 200
    return flight_total

def car_rental(days, daily_rate = 20):
    car_total = days * daily_rate
    return car_total

def holiday_cost(num_nights, flight, car_days):
    holiday_total = hotel_cost(num_nights) + plane_cost(flight) + car_rental(car_days)
    return holiday_total

# Graphics variables

staring_line = "\n───[Discount Holidays]─────────────────────────────────────────────\n"
bottom_line = "─────────────────────────────────────────────────────────────────"

# Taking input from the user and calling the functions 

while True:
    while True:
        print("\nHOTEL STAY\n")
        user_hotel = input("How many nights in the hotel: ")
        # Making sure that the user is inputting a valid value for nights in hotel
        if user_hotel.isdigit():
            # Converting the user input to int to allow it to be added to the night_rate in the hotel_cost() function
            user_hotel = int(user_hotel)
            break
        else:
            print("Your choice was not valid, type a valid number for days you want to stay in the Hotel!")
    while True:
        print('''
CITY CHOICE

You can now choose from the following cities to visit:

* Lisbon    ($150 Return Flight)
* Madrid    ($150 Return Flight)
* Amsterdam ($200 Return Flight)
* Berlin    ($200 Return Flight)
''')
        user_city = input("Type in the name of the city you will be visiting: ")
        # Making sure that the user types in a valid city name and making sure that the case matches the case expected by function plane_cost()
        if user_city.lower() == "lisbon" or user_city.lower() == "madrid" or user_city.lower() == "amsterdam" or user_city.lower() == "berlin":
            user_city = user_city.lower()
            break
        else:
            print("Please choose a valid city!")
    print('''
\nCAR RENTAL

Type 0 if you don't need a car otherwise type in the number of days you will need a car.''')
    user_car = input("How long will you need a car for: ")
    # Making sure that the user types in a valid city name and making sure that the case matches the case expected by function plane_cost()
    if user_car.isdigit():
        # Converting the user input to int to allow it to be added to the daily_rate in the car_rental() function
        user_car = int(user_car)
        break
    else:
        print("Number of days for the car please!!!!")

# Printing out user choices and breakdown of costs as well as total cost
print(staring_line)
print(f'''

Below is a summary of your choices and total costs:

Hotel:
    Num Nights:         {user_hotel}
    Cost:              ${hotel_cost(user_hotel)}

Flight:
    Destination:       {user_city.upper()}
    Cost:              ${plane_cost(user_city)}

Car:
    Num Days:           {user_car}
    Cost:              ${car_rental(user_car)}



Total Holidays Cost:   ${holiday_cost(user_hotel,user_city, user_car)}

''')

print(bottom_line)

print("Thank you for choosing Discount Holidays!")

