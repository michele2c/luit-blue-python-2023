"""
Project - EC2 Random Name Generator
"""
# **Use Case**

# Several departments share an AWS environment. You need to 
# ensure that the EC2s are properly named and are unique so team members 
# can easily tell who the EC2 instances belong to. Use Python to create 
# your unique EC2 names that the users can then attach to the instances. 

# The Python Script should:

# 1. All the user to input how many EC2 instances they want names for and output the same amount of unique names.

# 2. Allow the user to input the name of their department that is used in the unique name.

# 3. Generate random characters and numbers that will be included in the unique name.

# 4. Push your code to GitHub and include the link in your LinkedIn write up.

# marketing-e7b1682894434ec5890312c7c403c011

import random
import string

# using while loop

department_name = str(input("Department: "))
number_instances = int(input("Number of instances: "))

# initialize an empty list
instances_list = []
# initialize while loop counter
counter = 1

# while counter <= number_instances:
#     # initializing size of string
#     string_size = 32
#     # use random.choices() to randomly choose characters and numbers
#     # ''.join() to join the list of characters
#     random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=string_size))
#     # store department name in lowercase + random string
#     instances = department_name.lower() + "-" + random_name
#     # append result to the list
#     instances_list.append(instances)
 
#     counter += 1 #increment by 1


# print('This is your list:', instances_list)

# using for loop
num_instances = int(input("Number of instances: "))
dep_name = str(input("Department name: "))

# validate department name
if dep_name.lower() == "marketing" or dep_name.lower() == "accounting" or dep_name.lower() == "finops":
  # initialize list
    instances_list = []
    for x in range(num_instances):
      x += 1
      # define the lenght of the string
      str_size = 15
      # random part of the instance name
      random_name = ''.join(random.choices(string.hexdigits, k=str_size))
      # combine department and random name
      instance_name = dep_name.lower() + "-" + random_name.lower()
      # append names to the list
      instances_list.append(instance_name)
    print(instances_list)
else:
    print("Sorry! Your department cannot use this tool.")


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

