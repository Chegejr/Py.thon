# Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. 
# Equation of an area of a triangle is
 # Example 1
def calculate_area(x,y):
    shape_type = input('Press "s" for square or "r" for rectangle: ')
    if shape_type == "s":
        area= 1/2*(x*y)
        print("Area:",area)
    elif shape_type == "r":
        area= (x*y)
        print("Area:",area)

calculate_area(12,12)
# Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. 
# Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area.
# If no shape is supplied then it should take triangle as a default shape
# Example 2
def calculate_area(measurement1,measurement2,shape="triangle"):
    if shape == "triangle":
        area = 1/2*(measurement1*measurement2)
        print("Area of the",shape,"is",area)
    elif shape == "rectangle":
        area = measurement1*measurement2
        print("Area of the",shape,"is",area)
    else:
        print("Shape Error!")
calculate_area(12,12,"")

# Write a function called print_pattern that takes integer number as an argument and 
# prints pattern below if the input is 3
# *
# **
# ***
def print_pattern(n):
    for x in range(n):
        s= ""
        for j in range(x+1):
            s = s+"*"
        print(s)    

print_pattern(10)
