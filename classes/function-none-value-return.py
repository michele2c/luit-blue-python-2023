"""
None value
"""

# x = None
# if x is True:
#     print('None is True')
# elif x is False:
#     print('None is false')
# else:
#     print('None is just None')


# x = None
# if x is None:
#     print('yes')
# if x == None:
#     print('it does')

# # =========================================
# def greet():
#     print('Hello')

# x = greet()
# print(x) # function is returning anything

"""
Return
"""

def get_average(numbers):
    sum = 0.0
    for number in numbers:
        sum += number # sum = number + number
    average = sum / len(numbers) # sum divided by the amount of elements in the list
    return average # returning a value not just printing

# the function execution is terminate after the return

print(get_average([3.8, 4.2, 5.6]))

# storing the function in a variable
average = get_average([4, 8, 9, 3]) 
if average > 5:
    print('It is too high')


# Use Return to exit the function
def is_first_equal_last(number_list):
    if len(number_list) == 0:
        return # is condition does not match exit the function and return None value
    if (number_list[0] == number_list[-1]):
        return True
    else:
        return False

print(is_first_equal_last([10, 20, 30, 10]))
print(is_first_equal_last([10, 20, 30, 80]))
print(is_first_equal_last([]))