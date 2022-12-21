# Program that will output the number typed by the user (if bigger than 10)
# the number of times as the value of such number

num = int(input("Pick a number: "))

for i in range(0, num):
    if num <= 10:
        print(f"Sorry {num} is too small!") 
        break
    print(num)