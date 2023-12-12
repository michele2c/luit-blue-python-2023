"""
Your module description
"""
import string
import random

# initializing size of string
N = 7

# using random.choices()
# generating random strings
res = ''.join(random.choices(string.digits + string.ascii_lowercase, k=N))

# print result
print("The generated random string : " + str(res))



# N = 32
# random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N)
# print("The generated random string : " + str(random_name))