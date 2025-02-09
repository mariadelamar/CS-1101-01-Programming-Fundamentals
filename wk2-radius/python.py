import math 

def print_circum(radius):
    # Calculate the circumference and round it to 5 decimals
    circumference = 2 * math.pi * radius
    rounded_circumference = round(circumference, 5)
    
    # Print the result
    print("The circumference of a circle with a radius of " + str(radius) + " is " + str(rounded_circumference) + ".\n")

# Calling the function three times with different values for radius 
print_circum(5)
print_circum(100)
print_circum(2000)
