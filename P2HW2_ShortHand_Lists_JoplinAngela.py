# CTI-110
# P2HW2 - List
# Angela Joplin
# 10/10/2022
#
# Create a program to request and display test grades for modules 1-6.
# Query the list to display the lowest and highest grades and then the sum and average.

#input
grades = []
print('****** Module Test Scores ******')
grades.append(float(input('Enter grade for Module 1:  ')))
grades.append(float(input('Enter grade for Module 2:  ')))
grades.append(float(input('Enter grade for Module 3:  ')))
grades.append(float(input('Enter grade for Module 4:  ')))
grades.append(float(input('Enter grade for Module 5:  ')))
grades.append(float(input('Enter grade for Module 6:  ')))


#output
print()
print('************ Result ************')
print(f'Lowest Grade:     {min(grades):.2f}')
print(f'Highest Grade:    {max(grades):.2f}')
print(f'Sum of Grades:    {sum(grades):.2f}')
print(f'Average:          {sum(grades)/len(grades):.2f}')
print('********************************')
