# CTI-110
# P4HW2 - Salary Calculator
# Angela Joplin
# 11/14/2022

# Create lists to count number of employees entered and query for final calculations of totaly OT, regular and gross pay.
# Ask user for input for employee name, hours they have worked, and their pay rate. If a value of NONE is entered, end loop and
# display totals.Calculate if employees have overtime and if so, what the adjusted rate of pay will be and what regular pay is.
# Calculate gross pay given OT pay and regular pay. Display, name, hours worked,pay rate, OT hours, pay for OT, pay for regular
# hours, and gross pay. Once loop exits, display # of employees entered and thier combined ot, regular and gross pay.

name = ''
totalEmployees = []
count = 0
otPayList = []
regPayList = []
grossPayList = []

while name != 'NONE':
    name = (input("Enter employee's name or "'"NONE"'" to terminate: "))

    if name != 'NONE':
        hours = int(input(f"How many hours did {name} work? "))
        payRate = float(input(f"What is  {name}'s pay rate? "))


        otPayRate = payRate * 1.5
        if hours > 40:
            ot = hours - 40
            otPay = ot * otPayRate
            otPayList.append(otPay)
        else:
            ot = 0
            otPay = 0
        if hours <= 40:
            regPay = hours * payRate
            regPayList.append(regPay)
        else:
            regPay = (hours - ot) * payRate
            regPayList.append(regPay)
        gross = otPay + regPay
        grossPayList.append(gross)
        
        print()
        print('Employee Name:  ',name)
        print()
        print('Hours Worked   Pay Rate   OverTime    OverTime Pay       Regular Pay      Gross Pay')
        print('**************************************************************************************')
        print(f'     {hours}         ${payRate:.2f}        {ot}         ${otPay:.2f}            ${regPay:.2f}         ${gross:.2f}')
        print()
        print()
        count = count +1
    else:
        print(f'Total number of employees entered: {count}')
        print(f'Total amount payed for overtime: ${sum(otPayList):.2f}')
        print(f'Total amount paid for regular hours: ${sum(regPayList):.2f}')
        print(f'Total amount paid in gross: ${sum(grossPayList):.2f}')


