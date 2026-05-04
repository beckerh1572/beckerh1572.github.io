# Hannah Becker
# 03/11/2026
# P2HW2 - List Statistics
# This program asks the user to enter grades for six modules, stores them in a list,
# and then displays the lowest grade, highest grade, sum of grades, and average.

"""
PSEUDOCODE

1. Ask the user to enter grades for Module 1 through Module 6.
2. Convert each grade entered into a float.
3. Store all six grades into a list called module_grades.
4. Use Python functions to calculate:
      - lowest grade using min()
      - highest grade using max()
      - sum of grades using sum()
5. Calculate the average by dividing the sum by the number of grades.
6. Display the results formatted neatly with the average showing two decimal places.
"""

# Ask the user for module grades
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

# Store grades in a list
module_grades = [module1, module2, module3, module4, module5, module6]

print("\n------------Results------------")

# Display lowest grade
print(f"Lowest Grade: {min(module_grades)}")

# Display highest grade
print(f"Highest Grade: {max(module_grades)}")

# Display sum of grades
print(f"Sum of Grades: {sum(module_grades)}")

# Calculate average
average = sum(module_grades) / len(module_grades)

# Display average with two decimal places
print(f"Average: {average:.2f}")