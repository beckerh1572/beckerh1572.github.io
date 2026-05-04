# Hannah Becker
# 03/04/2026
# P2LAB2 - Dictionary and User Input
# This program uses a dictionary to store vehicle MPG values,
# allows the user to select a vehicle, and calculates gallons
# of gas needed for a specified number of miles.

# Create dictionary
vehicles = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Get all keys
keys = vehicles.keys()

# Print available vehicles
print(keys)

# Ask user to choose a vehicle
car = input("\nEnter a vehicle to see its mpg: ")

# Display mpg of selected vehicle
print(f"\nThe {car} gets {vehicles[car]} mpg.")

# Ask how many miles they will drive
miles = float(input(f"\nHow many miles will you drive the {car}? "))

# Calculate gallons needed
gallons_needed = miles / vehicles[car]

# Display gallons needed (rounded to 2 decimal places)
print(f"\nYou will need {gallons_needed:.2f} gallons of gas to drive the {car} {miles} miles.")