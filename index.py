import math
import random
import time

print("This program aims to estimate the maths constant 'pi' using the Monte Carlo method.")
print("A square with side = 2 and a circle with diameter 2 in it will be used.")
print("Concept: Ratio between area of circle to area of square equal ratio between number of points in circle to total number of points")
print("The estimation will be done for the number of times you decide")
print("The first time will use 10 points, each additional time, number of dots will increase by 10x")
print("This will also show how more points used leads to higher accuracy")
print()

def is_integer(input_str): # To check if users input an integer
    try:
        int(input_str)
        return True
    except ValueError:
        return False
    
check = False # A Flag variable to ensure that user inputs a positive integer

while not check:
    no_of_trials = (input("So, how many times do you want to estimate it (Recommended: 7) "))

    if  is_integer(no_of_trials):
        if int(no_of_trials) > 0:
            check = True
        else: 
                print("Invalid input. Please enter positive integers")
    else:
        print("Invalid input. Please enter positive integers")

print()
trial = 1 # Initialize for number of trials

while trial <= int(no_of_trials):  # Loop through user-specific number of times

    pts_in_circle = 0  # Initialize for the number of points in the circle for each iteration
    random.seed(time.time())   # Seed for uniqueness

    for i in range(10 ** trial):  # Loop "this" many times for each element in array "n" to get number of points
        
        # Generate a random float number between -1 and 1
        x = random.random()*2-1
        y = random.random()*2-1
        # We have our random coordinate now

        # Now we find the distance of the random point from (0,0), the centre
        distance = (x ** 2 + y ** 2) ** 0.5  # Pythagorean theorem

        if distance <= 1:  # If it's inside the circle
            pts_in_circle += 1  # Increment count of points in circle
    
    estimated_pi = 4 * (pts_in_circle / (10 ** trial))  # Estimate Pi
    print(f"Using {10**trial:,} points, estimated pi is {estimated_pi}, which has a percentage error of {abs(estimated_pi - math.pi) / math.pi * 100:.3f}%")

    trial += 1 # Onto next trial

print()
print("Note: For a circle with radius = 1, Area = Pi")
