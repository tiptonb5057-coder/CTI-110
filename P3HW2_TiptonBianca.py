# Bianca Tipton
# October 11, 2026
# P3HW2
# This program calculates an employee's weekly pay, including overtime.

# Get the employee's name
# Get their hours worked and pay rate
# See if they worked over 40 hours
# If they did, figure out how much overtime pay they earned
# If not, overtime pay is zero
# Figure out their regular pay
# Add everything together for their total pay
# Show the employee's pay information

# Get employee information
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Check for overtime
if hours > 40:
    overtime_hours = hours - 40
else:
    overtime_hours = 0

# Calculate regular pay
if hours > 40:
    regular_pay = 40 * pay_rate
else:
    regular_pay = hours * pay_rate

# Calculate overtime pay
overtime_pay = overtime_hours * pay_rate * 1.5

# Calculate total pay
gross_pay = regular_pay + overtime_pay

# Display employee pay information
print()
print("--------------------------------")
print("Employee name:", name)
print()
print("Hours Worked:", hours)
print("Pay Rate:", f"${pay_rate:.2f}")
print()
print("Overtime Hours:", overtime_hours)
print("Overtime Pay:", f"${overtime_pay:.2f}")
print("Regular Pay:", f"${regular_pay:.2f}")
print("Gross Pay:", f"${gross_pay:.2f}")
print("--------------------------------")