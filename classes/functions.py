"""
Functions
functions cannot be called before being defined
"""

# define a function
def greet():
    print('Hello, friend!')

# call function
greet()
greet()

"""
Functions Parameters and Arguments
"""
# numbers is the parameter
def get_average(numbers):
    sum = 0.0
    for number in numbers:
        sum += number # sum = number + number
    average = sum / len(numbers) # sum divided by the amount of elements in the list
    print(average)

# invoke the function and pass the argument
get_average([5.0, 3.5, 7.8, 9.9, 10.0])

"""
Function with 2 parameters
"""
# def letter_counter(text, letter):
#     counter = 0
#     for character in text:
#         if character == letter:
#             counter += 1
#     print(f'Number of letters {letter} is {counter}.')

# letter_counter('Today is Sunday and I am studiyng Python.', 'a')

# # using named arguments
# letter_counter(letter='s', text='sassaricando')

"""
Function with Default parameter value
"""
# add a default value to one or more parameters
def letter_counter(text, letter='a'):
    counter = 0
    for character in text:
        if character == letter:
            counter += 1
    print(f'Number of letters {letter} is {counter}.')

letter_counter('Calling with just one argument')