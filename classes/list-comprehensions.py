#list-comprehenssions
# numbers = [i for i in range(0, 11) if i % 3 != 0]
# print(numbers)

# ====================================================
# list comprehenssions ans nested list

# Create a table with 4 rows and 5 collumn
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
table = [[i for i in range(1, 6)] for j in range(4)]
print(*table, sep='\n')


# ====================================================
# list function
# num = list(range(0, 11))
# print(num)

