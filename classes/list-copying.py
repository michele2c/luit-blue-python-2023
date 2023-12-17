#copying lists

#  Use slicing to copy lists

list_original = [1, 2, 3]
list_copy = list_original[:]
list_original[0] = -5
print('Original:', list_original, '\nCopy:', list_copy)

# copy some elements
list_original = [1, 2, 3]
list_copy = list_original[:2]
list_original[0] = -5
print('Original:', list_original, '\nCopy:', list_copy)