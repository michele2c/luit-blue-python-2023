"""
Variables can be local - Scope inside the funtcion
or Global - outside the function
"""

# def show_truth():
#     mysterious_var = 'I am inside the function.'
#     print(mysterious_var)

# mysterious_var = 'Global variable'
# print(mysterious_var)
# show_truth()
# print(mysterious_var)


def show_truth():
    mysterious_var.append('I am inside the function.') # variable now it's declared only outside
    print(mysterious_var)

mysterious_var = ['Global variable']
print(mysterious_var)
show_truth()
print(mysterious_var)

