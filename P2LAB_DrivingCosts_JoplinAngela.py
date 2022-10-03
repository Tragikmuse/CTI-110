# Driving Cost program
# 9/26/2022
# CTI-110 P2LAB - Driving Costs
# Angela Joplin

# Create program that allows you to input miles per gallon (mpg) and
# price per gallon (ppg) and computes how much it costs to drive 20, 75 and 500
# miles based on that input. The lab submission does not allow for any text 
# prompts so this is as bare bones as it gets and essentially unuseable by
# anyone but the programmer. 

# With text prompts it makes more sense and would look as follows:
#input
#mpg = float(input('How many miles does your car get per gallon of gas? '))
#ppg = float(input("What is the price per gallon of gas? "))

#process
#miles20 = (20 / mpg) * ppg
#miles75 = (75 / mpg) * ppg
#miles500 = (500 / mpg) * ppg

#output
#print(f'It costs ${miles20:.2f} to drive 20 miles, ${miles75:.2f} to drive 75 miles , and ${miles500:.2f} to drive 500 miles.')



#input
mpg = float(input())
ppg = float(input())

#process
miles20 = (20 / mpg) * ppg
miles75 = (75 / mpg) * ppg
miles500 = (500 / mpg) * ppg

#output
print(f'{miles20:.2f} {miles75:.2f} {miles500:.2f}')
