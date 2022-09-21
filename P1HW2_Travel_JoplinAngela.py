# Travel Expense program
# 9/21/2022
#CTI-110 P1HW2 - Travel Expense
# Angela Joplin
#

# create var and get user input for budget, destination, gas, accomodatyions and food
# add expenses and subtract that from budget to show remaining budget balance
# display destination and var values for user and the remaining balance



print('This program calculates and displays travel expenses')

#Input
print()
budget = int(input('Enter Budget: '))
print()
loc = input('Enter your travel destination: ')
print()
gas = int(input('How much do you think you will spend on gas? '))
print()
accom = int(input('Approximately, how much will you need for accomodation/hotel? '))
print()
food = int(input('Last, how much do you need for food? '))

#Process
exp = gas + accom + food
remain = budget - exp


#Output
print()
print('*****Travel Expenses*****')
print('Location: ',loc)
print('Initial Budget: ',budget)
print()
print('Fuel: ',gas)
print('Accomodation: ',accom)
print('Food: ',food)
print()
print('Remaining Balance: ',remain)
      










