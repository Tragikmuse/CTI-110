# CTI-110
# P2HW2 - List
# Angela Joplin
# 10/10/2022
#
# Create a program to request and display test grades for modules 1-6.
# Query the list to display the lowest and highest grades and then the sum and average.

#input
print('****** Module Test Scores ******')
Mod1 = float(input('Enter grade for Module 1:  '))
Mod2 = float(input('Enter grade for Module 2:  '))
Mod3 = float(input('Enter grade for Module 3:  '))
Mod4 = float(input('Enter grade for Module 4:  '))
Mod5 = float(input('Enter grade for Module 5:  '))
Mod6 = float(input('Enter grade for Module 6:  '))

#process
grades = [Mod1, Mod2, Mod3, Mod4, Mod5, Mod6]
minGrd = min(grades)
maxGrd = max(grades)
sumGrd = sum(grades)
avgGrd = sumGrd/len(grades)

#output
print()
print('************ Result ************')
print(f'Lowest Grade:     {minGrd:.2f}')
print(f'Highest Grade:    {maxGrd:.2f}')
print(f'Sum of Grades:    {sumGrd:.2f}')
print(f'Average:          {avgGrd:.2f}')
print('********************************')

