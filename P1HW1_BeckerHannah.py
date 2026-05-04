# Online Python compiler (interpreter) to # Hannah Becker
# 02/28/2026
# P1HW1 - Mathematical Expressions
# This program collects integer input from the user, performs mathematical
# calculations (exponents, addition, and subtraction), and displays the results.

# Program Header
print("-----Calculating Exponents-----")

# Get base and exponent from user
base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

# Calculate power
result = base ** exponent

# Display result
print()
print(base, "raised to the power of", exponent, "is", result, "!!")

print()
print("-----Addition and Subtraction-----")

# Get three integers from user
num1 = int(input("Enter a starting integer: "))
num2 = int(input("Enter a second integer: "))
num3 = int(input("Enter a third integer: "))

# Perform calculations
sum_result = num1 + num2
final_result = sum_result - num3

# Display results
print()
print(f"{num1} + {num2} - {num3} is equal to {final_result}")
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")