import math
import random

print("This program aims to estimate the maths constant 'pi' using the Monte Carlo method.")
print("A square with dimensions 2x2 and a circle in it with diameter 2 will be used.")
print("Concept: Ratio between area of circle to area of square equal ratio between number of points in circle to total number of points")
print("The estimation will be done 5 times, with 10,000, 100,000, 1,000,000, 10,000,000, 100,000,000 points used respectively")
print("This will also show how more points used leads to higher accuracy")
print("(runtime is about a minute)")

n = [4, 5, 6, 7, 8]  # Array containing the number of points (10^n) to be generated for each value of n

for count in n:  # Loop through all values of n

    pts_in_circle = 0  # Initialize for the number of points in the circle for each iteration

    for i in range(10 ** count):  # Loop "this" many times for each element in array "n" to get number of points

        # Generate a random float number between -1 and 1
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        # We have our random coordinate now

        # Now we find the distance of the random point from (0,0), the centre
        distance = (x ** 2 + y ** 2) ** 0.5  # Pythagorean theorem

        if distance <= 1:  # If it's inside the circle
            pts_in_circle += 1  # Increment count of points in circle

    estimated_pi = 4 * (pts_in_circle / (10 ** count))  # Estimate Pi

    print(f"Using {10**count:,} points, estimated pi is {estimated_pi}, which has a percentage error of {abs(estimated_pi - math.pi) / math.pi * 100:.3f}%")
