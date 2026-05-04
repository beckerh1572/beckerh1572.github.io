# Hannah Becker
# 03/21/2026
# P3LAB - Money Breakdown
# This program takes a monetary amount and calculates the most efficient
# number of dollars, quarters, dimes, nickels, and pennies.

# Get user input
amount = float(input("Enter amount of money (e.g. 5.67): "))

# Convert to cents
cents = int(round(amount * 100))

# Calculate dollars
dollars = cents // 100
cents = cents - (dollars * 100)

# Calculate quarters
quarters = cents // 25
cents = cents - (quarters * 25)

# Calculate dimes
dimes = cents // 10
cents = cents - (dimes * 10)

# Calculate nickels
nickels = cents // 5
cents = cents - (nickels * 5)

# Remaining pennies
pennies = cents

# Display results
print("\nBreakdown:")

if dollars > 0:
    if dollars == 1:
        print("1 Dollar")
    else:
        print(dollars, "Dollars")

if quarters > 0:
    if quarters == 1:
        print("1 Quarter")
    else:
        print(quarters, "Quarters")

if dimes > 0:
    if dimes == 1:
        print("1 Dime")
    else:
        print(dimes, "Dimes")

if nickels > 0:
    if nickels == 1:
        print("1 Nickel")
    else:
        print(nickels, "Nickels")

if pennies > 0:
    if pennies == 1:
        print("1 Penny")
    else:
        print(pennies, "Pennies")