# CTI-110
# P3LAB - Leap Year
# Angela Joplin
# 10/10/2022

# Prompt user to input a year
# Determine if that year is a leap year based on being divisible by 4 and if the year is a century, if its divisible by 100 or 400
# Display whether or not the input is a leap year

   

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
