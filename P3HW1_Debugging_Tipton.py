# Bianca Tipton
# October 11, 2026
# P3HW1
# This program calculates the average of six grades.



# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = int(input('Enter grade for Module 1: '))
mod_2 = int(input('Enter grade for Module 2: '))
mod_3 = int(input('Enter grade for Module 3: '))
mod_4 = int(input('Enter grade for Module 4: '))
mod_5 = int(input('Enter grade for Module 5: '))
mod_6 = int(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

print()
print("Lowest Grade:", low)
print("Highest Grade:", high)
print("Sum of Grades:", total)
print("Average:", avg)

# determine letter grade for average


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





