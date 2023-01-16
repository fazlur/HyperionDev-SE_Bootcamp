# Creating Lists and dictionaries as per task requirements
menu = ['Coffee', 'Tea', 'Cake', 'Beer']

stock = {
        menu[0] : 10,
        menu[1] : 5,
        menu[2] : 1,
        menu[3] : 9
        }

price = {
        menu[0] : 1.30,
        menu[1] : 0.50,
        menu[2] : 3.99,
        menu[3] : 5.20,
        }
# Variable to hold total of stock value
total_stock_worth = 0

# Variables to hold display
staring_line = "\n───[INVENTORY]───────────────────────────────────────────────────\n"
menu_header = "ITEM\t\tUNITS\t\tPRICE\t\tTOTAL"
bottom_line = "─────────────────────────────────────────────────────────────────"

# Program execution
print(staring_line)
print(menu_header)

for item in menu:
    if item in stock.keys():
        total_stock_worth +=  (price[item] * stock[item])
        print(f'''
{item}\t\t{stock[item]}\t\t${price[item]}\t\t${round(price[item] * stock[item], 2)}''')

print("\n\nTotal Stock Worth: $"+str(round(total_stock_worth, 2)))

print(bottom_line)