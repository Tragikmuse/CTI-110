# CTI-110
# P3HW1 - Debugging
# Angela Joplin
# 10/24/2022


# Ask user to input 6 grades 
# Add grades entered to a list
# Calculate min, max, sum and average of grades
# Display min, max, sum and average of grades
# Determine and display letter grade for average

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

low = min(grades)
high = max(grades)
sum_all = sum(grades)
avg = sum_all/len(grades)


print()
print('************ Results ************')
print(f'Lowest Grade:     {low:.2f}')
print(f'Highest Grade:    {high:.2f}')
print(f'Sum of Grades:    {sum_all:.2f}')
print(f'Average:          {avg:.2f}')
print('********************************')


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

