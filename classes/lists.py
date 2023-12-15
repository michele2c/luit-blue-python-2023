"""
Types of collections - lists, tuples and dictionaries.
"""

top_cities = ['New York City', 'Los Angeles', 'Singapore','Chicago', 'Houston', 'Phoenix']
print(top_cities)

# indexing ===========================
print(top_cities[0]) # first element

print(top_cities[-1]) # last element

# =====================================

# Slicing 
print(top_cities[1:3])

print(top_cities[2:])

print(top_cities[:3])


# DELETING LIST ELEMENTS =============
del top_cities[2]
print(top_cities)

# Deleting wtih slicing ==============
del top_cities[3:]
print(top_cities)

# # Deleting the whole list ===========
# del top_cities[:]

# # deleting the variable =============
# del top_cities

# =====================================
# Adding new elements to lists
# .append() method

book_ratings = [7, 8, 9, 5, 6]
book_ratings.append(4)
print(book_ratings)

# .insert() method - take 2 arguments first index position and element
book_ratings.insert(1, 10)
print(book_ratings)