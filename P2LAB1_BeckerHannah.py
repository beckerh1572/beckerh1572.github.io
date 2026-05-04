# Hannah Becker
# 03/04/2026
# P2LAB1 - Variables and Expressions
# This program calculates the diameter, circumference, and area of a circle
# using a radius entered by the user.

import math

# Get radius from user
radius = float(input("Enter the radius of the circle: "))

# Calculate values
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Display results with proper formatting
print(f"\nDiameter: {diameter:.1f}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.3f}")