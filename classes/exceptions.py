"""
Try and except keywords to handles user input error and not get a error from python
"""
 
# try: # code that could raise exception
#     value = int(input('Enter an interger: '))
#     print('The inverse of', value, 'is', 1/value)

# except ValueError: # named the exception
#     # code that handles the exception / errors
#     print('You did not provide a number') # user input was not a interger

# except ZeroDivisionError:
#     print('0 is not divisible.')

# except: # any other expection is raised
#     print('Something went worng')

"""
Exeception propagation
"""

def get_day(user_info):
    day = int(input('What is the day of your birthday? '))
    user_info.append(day)

def get_month(user_info):
    month = int(input('What is the month of your birthday? '))
    user_info.append(month)

def get_year(user_info):
    year = int(input('What is the year of your birthday '))
    user_info.append(year)

def get_user_bday(user_info):
    try:
        get_day(user_info)
        get_month(user_info)
        get_year(user_info)
        print('So your birthday is', user_info)
    except ValueError:
        print('Invalid information.')

print('Hi, I will collect some information.')
user_info = []
get_user_bday(user_info)