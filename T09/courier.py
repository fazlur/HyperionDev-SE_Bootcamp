#Creating all options setting them as False by default
air_delivery = False
full_insurance = False
gift = False
priority = False

#Getting the package cost and delivery distance
cost_of_package = float(input("How much does the package cost: "))
distance_km = float(input("How far the delivery in KM: "))

#Checking with the user what options and extras are to be set
air_delivery_check = input("Type yes for air delivery, otherwise the delivery will be by freight: ")
if(air_delivery_check.lower() == "yes"):
    air_delivery = True
    delivery_cost_km = 0.36
else:
    delivery_cost_km = 0.25

insurance_check = input("Type yes for full insurance, otherwise the delivery will be with limited insurance: ")
if(insurance_check.lower() == "yes"):
    full_insurance = True
    insurance_cost = 50
else:
    insurance_cost = 25

gift_check = input("Type yes if this is a gift: ")
if(gift_check.lower() == "yes"):
    gift = True
    gift_cost = 15
else:
    gift_cost = 0

priority_check = input("Type yes for priority delivery, otherwise it will be standard delivery: ")
if(priority_check.lower() == "yes"):
    priority = True    
    priority_cost = 100
else:
    priority_cost = 20

#Displaying all options chosen 
# and costs they incur 
print(f"""
Package cost: \t\t R{cost_of_package}
Delivery cost per KM: \t R{delivery_cost_km}
Insurance cost: \t R{insurance_cost}
Gift cost: \t\t R{gift_cost}
Priority cost: \t\t R{priority_cost}

Total cost: \t\t R{(distance_km * delivery_cost_km) + insurance_cost + gift_cost + priority_cost + cost_of_package}
""")

