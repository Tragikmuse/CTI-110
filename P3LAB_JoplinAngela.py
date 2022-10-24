# CTI-110
# P3LAB - Leap Year
# Angela Joplin
# 10/10/2022

# Write program to determine if a given year is or is not a leap year
# based on whether its divisible by 4 and is a century divisible by 400

   

#Input
input_year = int(input('Enter year to determine if it is a leap year: '))

#Process
if (input_year % 4) == 0:
    if (input_year % 100) == 0:
        if (input_year % 400) == 0:
            is_leap_year = True
        else:
            is_leap_year = False
    else:
        is_leap_year = True  
else:
    is_leap_year = False



#Output
if is_leap_year == True:    
    print(f'{input_year} is a leap year.')
else:
    print(f'{input_year} is not a leap year.')
