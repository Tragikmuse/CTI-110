# CTI-110
# P5LAB1 - Leap Year
# Angela Joplin
# 11/21/2022

#user_year = int(input('Enter year to determine the number of days in February that year: '))

user_year = int(input())

def days_in_feb(user_year):
    if((user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0)):
        print(f'{user_year} has 29 days in February.')
    else:
        print(f'{user_year} has 28 days in February.')

days_in_feb(user_year)    

# do i loop for multiple inputs?

'''
def days_in_feb(user_year):
    if (user_year % 4) == 0:
        if (user_year % 100) == 0:
            if (user_year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


if (days_in_feb(user_year)):
        print(f'{user_year} has 29 days in February.')
else:
        print(f'{user_year} has 28 days in February.')
'''        
'''        
def days_in_feb(user_year):
    if (user_year % 4) == 0:
        if (user_year % 100) == 0:
            if (user_year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

user_year = int(input())

while (user_year) != 0:
    if (days_in_feb(user_year)):
        print(f'{user_year} has 29 days in February.')
        user_year = int(input())
    else:
        print(f'{user_year} has 28 days in February.')
        user_year = int(input())

        
'''
