# Travel Expense (Revised)
# 9/26/2022
# CTI-110 P2HW1 - Travel
# Angela Joplin
#

# create var and get user input for budget, destination, gas, accomodatyions and food
# add expenses and subtract that from budget to show remaining budget balance
# display destination and var values for user and the remaining balance
# revise P1HW2 to reflect float values and dollar signs for monetary variables



print('This program calculates and displays travel expenses')

#Input
print()
budget = float(input('Enter Budget: '))
print()
loc = input('Enter your travel destination: ')
print()
gas = float(input('How much do you think you will spend on gas? '))
print()
accom = float(input('Approximately, how much will you need for accomodation/hotel? '))
print()
food = float(input('Last, how much do you need for food? '))

#Process
exp = gas + accom + food
remain = budget - exp


#Output
print()
print('*********Travel Expenses*********')
print('Location:          ',loc)
print('Initial Budget:     $',budget)
print('Fuel:               $',gas)
print('Accomodation:       $',accom)
print('Food:               $',food)
print('---------------------------------')
print('Remaining Balance:  $',remain)
