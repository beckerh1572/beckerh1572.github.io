# Hannah Becker
# 2026-04-02
# P4LAB2
# Program displays multiplication tables for non-negative integers and handles negative input.

run_again = "yes"  # Initialize variable to enter the while loop

while run_again.lower() == "yes":
    # Ask the user for an integer
    num = int(input("Enter an integer: "))

    if num >= 0:
        print(f"Multiplication table for {num}:")
        # For loop for multiplication table from 1 to 12
        for i in range(1, 13):
            print(f"{num} * {i} = {num * i}")
    else:
        print("Cannot accept negative values.")

    # Ask user if they want to run the program again
    run_again = input("Do you want to run the program again? (yes/no): ")

print("Program ended.")