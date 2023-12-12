"""
type casting
"""
# type conversion, which means changing from strings to floats or from integer to strings is often called typecasting.


# using float()
# height_cm = float(input('Height converter: Enter your height in cm: '))
# print(f'Your height in feet is: {height_cm / 30.48}')


# using int() integer
# year_born = int(input('What year were you born? '))
# print(f'In 2100, you will be {2100 - year_born} years old!')

# using str() string
temp_c = input('Enter temperature in Celsius degrees: ')
temp_f = float(temp_c) * 1.8 + 32
temp_statement = str(temp_c) + ' degrees Celsius equals ' + str(temp_f) + ' degrees Fahrenheit.'
print(temp_statement)
