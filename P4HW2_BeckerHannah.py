# Your Name: Hannah Becker
# Date: 04/12/2026
# Assignment Name: P4HW2
# Description: This program calculates gross pay for multiple employees,
# including overtime and regular pay. It also keeps running totals and
# displays summary results when the user enters "Done".

"""
PSEUDOCODE:

1. Initialize totals:
    total_overtime_pay = 0
    total_regular_pay = 0
    total_gross_pay = 0
    employee_count = 0

2. Ask user for employee name

3. WHILE employee name is not "Done":
    a. Ask for hours worked
    b. Ask for pay rate

    c. IF hours > 40:
        overtime_hours = hours - 40
        regular_hours = 40
    ELSE:
        overtime_hours = 0
        regular_hours = hours

    d. Calculate:
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        regular_pay = regular_hours * pay_rate
        gross_pay = overtime_pay + regular_pay

    e. Add to totals:
        total_overtime_pay += overtime_pay
        total_regular_pay += regular_pay
        total_gross_pay += gross_pay
        employee_count += 1

    f. Display employee pay details

    g. Ask for next employee name

4. When user enters "Done":
    Display:
        total number of employees
        total overtime pay
        total regular pay
        total gross pay
"""

# Initialize totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

# First input
employee_name = input("Enter employee's name or 'Done' to terminate: ")

# Loop using sentinel
while employee_name != "Done":

    hours = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))

    # Overtime calculation
    if hours > 40:
        overtime_hours = hours - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours

    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = regular_hours * pay_rate
    gross_pay = overtime_pay + regular_pay

    # Add to totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    # Display employee details
    print("\nEmployee name:  ", employee_name)
    print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<12}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<10}")
    print("------------------------------------------------------------------------------------------")
    print(f"{hours:<15.2f}{pay_rate:<12.2f}{overtime_hours:<12.2f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:<10.2f}")

    # Ask for next employee
    employee_name = input("\nEnter employee's name or 'Done' to terminate: ")

# Final totals output
print("\n----------------------------")
print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")