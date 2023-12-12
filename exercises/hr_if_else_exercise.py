"""
Task
Given an integer,n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5,print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
"""
import random

n = random.randint(1, 25)

if n % 2 == 0:
    if n >= 6 and n < 21:
        print(n, 'Weird')
    else:
        print(n, 'Not Weird')
    
else:
    print(n, 'Weird')
    