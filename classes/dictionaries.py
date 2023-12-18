"""
Dictionaries - Type of Collection
pair of key and value
{
    'key': 'value'
}
"""

emails = {
    'Anna Hall': 'ahall@example.com',
    'Mike Brown': 'mbrown@example.com',
    'Peter Pan': 'ppan@example.com' 
}
print(emails['Anna Hall'])

portuguese_animals = {
    'dog': 'cachorro',
    'cat': 'gato',
    'horse': 'cavalo',
    'bird': 'pássaro'
}
print(portuguese_animals['dog'])

# key must be immutable
# value can be any data type
grades = {
    'Mike': [7, 8, 9],
    'Paula': [10, 9 ,10],
    'John': [9, 8, 6]
}

"""
Dictionary opearations
"""
# empty dictionary
grades_high_school = {}

# adding entries
# variable ['key'] = 'value
grades_high_school['Paul'] = 'A-'
grades_high_school['Kim'] = 'A'
grades_high_school['Erin'] = 'B'
print(grades_high_school)

# Update dictioonary
grades_high_school['Paul'] = 'B'

# update using .update method
grades_high_school.update({'Kim':'C'})

print(grades_high_school)

# checking the number of entries usding len()
print(len(grades_high_school))

# checking presence of a key
if 'Kim' in grades_high_school:
    print('Kim got', grades_high_school['Kim'])

# delete entry
del grades_high_school['Paul']
print(grades_high_school)

"""
Iterating on the dictionary
"""
for element in grades_high_school:
    print(element)

# using .keys() method
for element in grades_high_school.keys():
    print('key:',element)

# .values() method
for element in grades_high_school.values():
    print('value:',element)

# .items() method return key and value
for student, grade in grades_high_school.items():
    print(student, 'got', grade)

