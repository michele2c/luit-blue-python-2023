"""
Project - EC2 Random Name Generator
"""
# Use the input of the number of instances as an argument in a “while loop”.

# Inside the loop, I'm going to use the random library to generate the random part of the instance’s name and concatenate this output with the department name output, creating a new string ((marketing_1209873) that will be stored in a variable.

# When the “while loop” reaches its condition (the number of instances desired), it will print out all the unique names in sequence.

# marketing-e7b1682894434ec5890312c7c403c011

import random


department_name = str(input("Department: "))
number_instances = int(input("Number of instances: "))

counter = 1
instances_list = []
while counter <= number_instances:
    number = random.randint(100, 10000000)
    instances = department_name.lower() + '_' + str(number)
    # print(instances)
    instances_list.append(instances)
 
    counter += 1 #increment by 1


print(instances_list)

# number = random.randint(100, 10000000)
# print(number)



# print(department_name, number, sep='_')


# counter = 1
# while counter < 11:
#     print(counter)
#     counter += 1 # increment by 1
# print('Done!')

# first_name = "John"
# last_name = "Doe"

# print("".join([first_name, last_name]))
# # JohnDoe