# Hannah Becker
# 03/11/2026
# P2HW1 - Travel Expenses
# This program asks the user for travel expenses and displays a formatted travel expense report.

# Get user input
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculate remaining balance
expenses = gas + accommodation + food
remaining = budget - expenses

print("\n------------Travel Expenses------------")
print(f"{'Location:':20}{destination}")
print(f"{'Initial Budget:':20}${budget:.2f}")
print()

print(f"{'Fuel:':20}${gas:.2f}")
print(f"{'Accommodation:':20}${accommodation:.2f}")
print(f"{'Food:':20}${food:.2f}")
print()

print(f"{'Remaining Balance:':20}${remaining:.2f}")