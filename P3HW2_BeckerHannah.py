# Hannah Becker
# 03/29/2026
# P3HW2 - Salary Calculation with Overtime
# This program calculates an employee's pay including overtime using decision structures.

"""
Pseudocode (Algorithm):

1. Ask user to enter employee name
2. Ask user to enter number of hours worked
3. Ask user to enter pay rate

4. If hours worked is greater than 40:
      overtime_hours = hours_worked - 40
      regular_hours = 40
   Else:
      overtime_hours = 0
      regular_hours = hours_worked

5. Calculate overtime pay:
      overtime_pay = overtime_hours * (pay_rate * 1.5)

6. Calculate regular pay:
      regular_pay = regular_hours * pay_rate

7. Calculate gross pay:
      gross_pay = regular_pay + overtime_pay

8. Display:
      Employee name
      Pay rate
      Hours worked
      Overtime hours
      Overtime pay
      Regular pay
      Gross pay
"""

# Get user input
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Determine overtime
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

# Calculate pay
overtime_pay = overtime_hours * (pay_rate * 1.5)
regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

# Display results
print("\n----------------------------------------")
print(f"Employee name:     {employee_name}")
print("----------------------------------------")
print(f"{'Hours Worked:':20}{hours_worked:>10.2f}")
print(f"{'Pay Rate:':20}${pay_rate:>9.2f}")
print(f"{'Overtime Hours:':20}{overtime_hours:>10.2f}")
print(f"{'Overtime Pay:':20}${overtime_pay:>9.2f}")
print(f"{'Regular Pay:':20}${regular_pay:>9.2f}")
print("----------------------------------------")
print(f"{'Gross Pay:':20}${gross_pay:>9.2f}")