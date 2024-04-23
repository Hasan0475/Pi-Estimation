import math
import random
import time

def is_float(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False

def is_positive(input_num):
    return float(input_num) > 0

def is_integer(input_str):
    try:
        int(input_str)
        return True
    except ValueError:
        return False

check_radius = False
check_points = False

# Prompt the user to enter the number of points to use in each trial
while not check_points:
    no_of_points = input("Input number of trial in simulation: ")

    if is_integer(no_of_points) and is_positive(no_of_points):
        check_points = True
    else:
        print("Invalid input. Please enter a positive integer for the number of points.")

# Prompt the user to enter the radius of the circle
while not check_radius:
    radius = input("Input the radius of the circle: ")

    if is_float(radius) and is_positive(radius):
        check_radius = True
    else:
        print("Invalid input. Please enter a positive number for the radius.")

print()

pts_in_circle = 0

random.seed(time.time())

for i in range(int(no_of_points)):
    x = random.random() * 2 * float(radius) - float(radius)
    y = random.random() * 2 * float(radius) - float(radius)
    distance = (x ** 2 + y ** 2) ** 0.5
    if distance <= float(radius):
        pts_in_circle += 1

estimated_area = (pts_in_circle / int(no_of_points)) * ((2 * float(radius)) ** 2)
actual_area = math.pi * (float(radius) ** 2)
percentage_error = abs((estimated_area - actual_area) / actual_area) * 100

print("Number of times in circle is", pts_in_circle)
print("Number of times out of circle is", int(no_of_points) - pts_in_circle)
print(f"Actual Area of circle is {estimated_area:.3f}")
print(f"Actual Area of circle is {actual_area:.3f}")
print(f"Percentage error is: {percentage_error:.3f}%")
