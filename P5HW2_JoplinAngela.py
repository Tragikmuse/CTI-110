# Menu driven simple math quizzes
# 11/23/2022
# CTI-110 P5HW2 - Math Quiz
# Angela Joplin
#

print('Welcome to Math Quiz')
print()
print()

# need to make these options chooseable and main menu display, have this loop
# until 3 is pressed, says to make a module/file containing the menu but we havent done this.
# i'm sure some functions should be here but not sure where.
'''
while user_selection != 3: # user_selection is not defined so this doesnt work
'''
print('MAIN MENU')
print('********************************')
print('1. Adding Random Numbers')
print('2. Subtracting Random Numbers')
print('3. Exit')
print()
user_selection = int(input('Please choose one of the menu options: '))


import random

num1 = random.randint(1, 1000)
num2 = random.randint(1, 1000)

if user_selection == 1:
    g = 0
    print('  ', num1)
    print('+ ', num2)
    print()
    user_answer1 = int(input('Enter your answer\n'))
    
    while user_answer1 != num1 + num2: 
       
        if user_answer1 < num1 + num2:
            print('Sorry, your guess is too low')
            g = g + 1
            print()
            user_answer1 = int(input('Try again\n'))
                               
        elif user_answer1 > num1 + num2:
            print('Sorry, your guess is too high')
            g = g + 1
            print()
            user_answer1 = int(input('Try again\n'))
                               
        else:
            print('Your answer is invalid.')
            user_answer1 = int(input('Please try again\n'))
            
    print('Congratulations!!!! You are correct!')
    g = g + 1
    print('Number of guesses: ', g)
        

elif user_selection == 2:
    g = 0
    print('  ', num1)
    print('- ', num2)
    print()
    user_answer1 = int(input('Enter your answer\n'))
    
    while user_answer1 != num1 - num2:
         
        if user_answer1 < num1 - num2:
            print('Sorry, your guess is too low')
            g = g +1
            print()
            user_answer1 = int(input('Try again\n'))
        
        elif user_answer1 > num1 - num2:
            print('Sorry, your guess is too high')
            g = g + 1
            print()
            user_answer1 = int(input('Try again\n'))
        
        else:
            print('Your answer is invalid.')
            user_answer1 = int(input('Please try again\n'))

    print('Congratulations!!!! You are correct!')
    g = g + 1
    print('Number of guesses: ', g)    
        
elif user_selection == 3:
    print('Thank you for playing...')
    print('Goodbye!')

else:
    user_selection = int(input('Error, please make a valid selection: '))
# need to loop back to menu selection in case of an invalid selection
