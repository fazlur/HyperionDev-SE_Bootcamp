#Checking with the user the shape and info required to calculate the area
while True:
    shape = input("""
Type A, B or C to chose the shape you want to calculate the area for:
    
A. Square
B. Rectangle
C. Circle
""")
    #asking the user for the relevant info to put in the area calculation
    if shape.upper() == "A":
        length = float(input("You have chosen Square, give us the length of one of the sides please: "))
        area = length * length
        print(f"The area of your square is {round(area, 2)}")
        break
    elif shape.upper() == "B":
        print("You have chosen Rectangle.")
        length = float(input("What is the length of the rectangle: "))
        width = float(input("What is the width of the rectangle: "))
        area = length * width
        print(f"The area of your rectangle is {round(area, 2)}")
        break
    elif shape.upper() == "C":
        radius = float(input("You have chosen Circle, give us the radius of your circle: "))
        import math
        area = math.pi * (radius * radius)
        print(f"The area of your circle is {round(area, 2)}")
        break
    else:
        print(f"Your choice {shape} is not valid, choose a valid option.")