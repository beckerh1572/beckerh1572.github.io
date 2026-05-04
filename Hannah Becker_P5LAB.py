# Hannah Becker
# 04/25/2026
# P5LAB - Self Checkout Change Dispenser
# This program simulates a self-checkout machine. It generates a random total,
# accepts user payment, calculates change, and displays the number of dollars,
# quarters, dimes, nickels, and pennies to return.

import random

def disperse_change(change):
    cents = int(round(change * 100))

    if cents == 0:
        print("No change owed.")
        return

    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    print("\nChange to be returned:")

    if dollars > 0:
        print(f"Dollars: {dollars}")
    if quarters > 0:
        print(f"Quarters: {quarters}")
    if dimes > 0:
        print(f"Dimes: {dimes}")
    if nickels > 0:
        print(f"Nickels: {nickels}")
    if pennies > 0:
        print(f"Pennies: {pennies}")


def main():
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Total owed: ${total_owed:.2f}")

    # Input validation loop
    while True:
        try:
            user_input = input("Enter amount of cash provided: $")

            if user_input.strip() == "":
                print("Input cannot be blank. Please enter a value.")
                continue

            cash = float(user_input)

            if cash < total_owed:
                print("Not enough money. Please enter a valid amount.")
            else:
                break

        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting.")
            return

    change = round(cash - total_owed, 2)
    print(f"Change owed: ${change:.2f}")

    disperse_change(change)


# Call main function
main()