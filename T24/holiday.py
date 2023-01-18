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

def holiday_cost(num_nights, flight, car_days):
    holiday_total = num_nights + flight + car_days
    return holiday_total

user_hotel = int(input("How many nights in the hotel: "))
user_city = input("Which city you will be visiting: ")
user_car = int(input("How long will you need a car for: "))

hotel = hotel_cost(user_hotel)
city = plane_cost(user_city)
car = car_rental(user_car)

print(hotel)
print(city)
print(car)

print(holiday_cost(hotel,city, car))

