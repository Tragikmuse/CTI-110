
# Simple Statistics program
# 10/3/2022
# CTI-110 P2LAB - Simple Statistics
# Angela Joplin

# Create program that allows you to input numbers and computes the product and 
# average in both an integer and 3 decimal float based on the initial input.


#input
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

#process
product = num1 * num2 * num3 * num4
avg = (num1 + num2 + num3 + num4) / 4

#output
print(f'{product:.0f} {avg:.0f}')
print(f'{product:.3f} {avg:.3f}')
