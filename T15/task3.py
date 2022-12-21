# Creating a while loop that counts down from 20 to 0
count = 20
print("""
Counting backwarwards from 20 to 0
-----------------------------------
""")
while count >= 0:
    print(count)
    count -= 1

# Creating a loop that displays even numbers between 1 and 20
print("""
Printing all even numbers between 1 and 20
-------------------------------------------
""")
for num in range(1, 21):
    if(num % 2 == 0):
        print(num)

# Loop to print 1 to 5 asteriscs incrementally 
print("""
Printing 1 to 5 asteriscs incrementally
---------------------------------------
""")
for i in range(1, 6):
    print(i * "*")

# Fiding the greatest common divisor(gcd)
print("""
Insert two numbers to find the greatest common divisor between them
--------------------------------------------------------------------
""")
num1 = int(input("Type in the first number: "))
num2 = int(input("Type in the second number: "))

while num2 != 0:
    gcd = num2
    num2 = num1 % num2
    num1 = gcd

print(gcd)