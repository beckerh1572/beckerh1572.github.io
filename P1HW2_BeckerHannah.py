# Hannah Becker
# 02/28/2026
# P1HW2 - Travel Budget Calculator
# This program asks the user to enter a travel budget and planned expenses,
# calculates total expenses, and displays the remaining balance.

"""
Pseudocode:

1. Display program title
2. Ask user to enter their total travel budget
3. Ask user to enter travel destination
4. Ask user to enter gas expense
5. Ask user to enter accommodation expense
6. Ask user to enter food expense
7. Add all expenses together
8. Subtract total expenses from budget
9. Display destination, budget, expenses, and remaining balance
"""

# Display program title
print("------Travel Budget Calculator------")
print()

# Get user inputs
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("Enter amount you will spend on gas: "))
accommodation = float(input("Enter amount you will spend on accommodation: "))
food = float(input("Enter amount you will spend on food: "))

# Calculate expenses and remaining balance
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

# Display results
print()
print("------Travel Expenses------")
print("Location:", destination)
print("Initial Budget:", budget)

print()
print("Gas:", gas)
print("Accommodation:", accommodation)
print("Food:", food)

print()
print("Remaining Balance:", remaining_balance)