# Bianca Tipton
# October 11, 2026
# P3LAB
# This program figures out how many dollars and coins make up an amount of money.

# Ask for an amount of money
# Turn the amount into cents
# Figure out how many dollars there are
# See how many quarters, dimes, nickels, and pennies are left
# Don't show any coins if there aren't any
# Make sure the coin names are singular or plural

# Get the amount of money
money = float(input("Enter an amount of money: "))

# Change money into cents
cents = round(money * 100)

# Figure out the dollars
dollars = cents // 100
cents = cents - (dollars * 100)

# Figure out the quarters
quarters = cents // 25
cents = cents - (quarters * 25)

# Figure out the dimes
dimes = cents // 10
cents = cents - (dimes * 10)

# Figure out the nickels
nickels = cents // 5
cents = cents - (nickels * 5)

# Figure out the pennies
pennies = cents

# Show the dollars
if dollars == 1:
    print("1 Dollar")
elif dollars > 1:
    print(dollars, "Dollars")

# Show the quarters
if quarters == 1:
    print("1 Quarter")
elif quarters > 1:
    print(quarters, "Quarters")

# Show the dimes
if dimes == 1:
    print("1 Dime")
elif dimes > 1:
    print(dimes, "Dimes")

# Show the nickels
if nickels == 1:
    print("1 Nickel")
elif nickels > 1:
    print(nickels, "Nickels")

# Show the pennies
if pennies == 1:
    print("1 Penny")
elif pennies > 1:
    print(pennies, "Pennies")