#Getting the name of the products from the user
product_one = input("What is the first product: ")
product_two = input("What is the second product: ")
product_three = input("What is the third product: ")

#Getting the price of the products from the user
price_product_one = float(input("Whats is the price of the first product: "))
price_product_two = float(input("Whats is the price of the second product: "))
price_product_third = float(input("Whats is the price of the third product: "))

#Calculating the total price by summing the price of the 3 products
total_price = price_product_one + price_product_two + price_product_third

#Calculating the average price by dividing the total price by the number of products
average_price = total_price / 3

#Using the f-string to output the product names, total and average price by passing those values to the round() method to limit the result to 2 decimal places
print(f"The Total of {product_one}, {product_two}, {product_three} is R{round(total_price, 2)} and the average price of the items is R{round(average_price, 2)}")
