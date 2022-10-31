# CTI-110
# P3HW2 - Salary
# Angela Joplin
# 10/24/2022

# Ask user for input for an employee name, hours they have worked, and their pay rate.
# Calculate if employee has overtime and if so, what the adjusted rate of pay will be and what regular pay is.
# Calculate gross pay given OT pay and regular pay.
# Display, name, hours worked,pay rate, OT hours, pay for OT, pay for regular hours, and gross pay.

#input
name = (input("Enter employee's name: "))
hours = int(input('Enter number of hours worked: '))
payRate = float(input("Enter employee's pay rate: "))

#process
otPayRate = payRate * 1.5
if hours > 40:
    ot = hours - 40
    otPay = ot * otPayRate
else:
    ot = 0
    otPay = 0
if hours <= 40:
    regPay = hours * payRate
else:
    regPay = (hours - ot) * payRate
gross = otPay + regPay
    
#output
print('**************************************************')
print('Employee Name:  ',name)
print()
print('Hours Worked   Pay Rate   OverTime    OverTime Pay       Regular Pay      Gross Pay')
print('**************************************************************************************')
print(f'     {hours}         ${payRate:.2f}        {ot}         ${otPay:.2f}            ${regPay:.2f}         ${gross:.2f}')
