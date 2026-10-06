# Bianca Tipton
# October 5, 2026
# P1HW2
# This program calculates a travel budget and expenses.

# Get the user's budget.
# Get the travel destination.
# Get the gas, hotel, and food costs.
# Add all the expenses together.
# Subtract expenses from the budget.
# Display the results.

budget = float(input("Enter your budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much will you spend on gas? "))
hotel = float(input("How much will you spend on accommodation? "))
food = float(input("How much will you spend on food? "))

total_expenses = gas + hotel + food
remaining_balance = budget - total_expenses

print()
print("Travel Expenses")
print("Location:", destination)
print("Initial Budget:", budget)
print("Gas:", gas)
print("Accommodation:", hotel)
print("Food:", food)
print("Remaining Balance:", remaining_balance)