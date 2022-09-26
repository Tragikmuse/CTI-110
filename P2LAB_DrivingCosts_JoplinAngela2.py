print('   ','**********Driving Costs**********')

miles = float(input('How many miles driven? '))
mpg = float(input('How many miles per gallon does your car get? '))
ppg = float(input('How much do you pay for a gallon of gas? '))

gasCost = (miles / mpg) * ppg

print('It will take $', ('{:.2f}'.format(gasCost)), 'to drive ', miles, 'miles.')

print(f'{miles:.2f} {mpg:.2f} {ppg:.2f}')
