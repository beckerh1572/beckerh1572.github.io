# Hannah Becker
# 03/29/2026
# P3LAB - Grade Calculator
# This program takes grades for six modules, calculates the average,
# and displays the corresponding letter grade.

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum, and average
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

# Display results
print("\n------------Results------------")
print(f"Lowest Grade: {low}")
print(f"Highest Grade: {high}")
print(f"Sum of Grades: {total}")
print(f"Average: {avg:.2f}")

# Determine letter grade
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')