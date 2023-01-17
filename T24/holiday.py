# Defining Functions

def hotel_cost(nights, night_rate = 100):
    hotel_total = nights * night_rate
    return hotel_total

def plane_cost(city):
    if city == "Lisbon":
        flight_total = 150
    elif city == "Madrid":
        flight_total = 150
    elif city == "London":
        flight_total = 200
    elif city == "Berlin":
        flight_total = 200
    return flight_total

def car_rental(days, daily_rate = 20):
    car_total = days * daily_rate
    return car_total

def holiday_cost(num_nights, city, car_days):
    holiday_total = holiday_cost(num_nights) + plane_cost(city) + car_rental(car_days)
    return holiday_total

user_hotel = input("How many nights in the hotel: ")
#user_city = input("Which city you will be visiting: ")
#user_car = input("How long will you need a car for: ")

print(hotel_cost(user_hotel))

