"""
Tuples - type of collection
Tuples are often used when you want to group together values of different types that are
somehow related, and together they form some sort of structure.
"""

# empty_tuple = ()
# # element tuple
# one_element_a = (1,)
# one_element_b = 1,

# # more than one elements
# three_elements = 1, 2, 3
# print(three_elements)


# tuples are immmutable
# it can be reassinged but not changed as lists (list are mutable)
 
# user_data = ('John', 'american', 1964)
# print(user_data)
# user_data = ('Carl', 'french', 1988)
# print(user_data)

#=================================================================
# Tuples Opearations

# user_data = ('Carl', 'french', 1988)
# print(len(user_data))


# user_data = ('Carl', 'french', 1988)
# if 'french' in user_data:
#     print('This person is french')


# user_data = ('Carl', 'french', 1988)
# for element in user_data:
#     print(element)

# user_data = ('Carl', 'french', 1988) + ('teacher', 'male')
# print(user_data)


# =======================================================
# Tuples in lists and list in Tuples

city_1 = ('London', 'UK', 8.98)
city_2 = ('Canberra', 'Australia', 0.4)
city_3 = ('Algiers', 'Algeria', 3.9)
# tuples inside a list
capitals = [('London', 'UK', 8.98),('Canberra', 'Australia', 0.4), ('Algiers', 'Algeria', 3.9)]
for capital in capitals:
    print('Name:', capital[0], ' Country:', capital[1], ' Population:', capital[2])


# list inside a tuple
user_data = ('Carl', 'french', 1988, [77.0, 78.1, 69.9])
# adding elements to the list inside the tuple
user_data[3].append(80.0)
print(user_data)