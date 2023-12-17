# list and sublist

cells = [['A1', 'A2', 'A3'], ['B1','B2','B3']]
print(cells[0][2]) # print A3

print(cells[1][1]) # print B2

for i in cells:
    print('Element: ', i)

#==================================================
# NESTED LISTS
table = [['A1', 'A2', 'A3'], ['B1','B2','B3']]
for row in table:
    for cell in row:
        print('Element: ', cell)  

#==================================================
# list comprehenssions ans nested list

# Create a table with 4 rows and 5 collumn
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
table = [[i for i in range(1, 6)] for j in range(4)]
print(*table, sep='\n')

#==================================================
# multiply lists
numbers = [0, 1, 2] * 5
print(numbers)

vegetables = ['cucumber', 'onion', 'carrot']
fruits = ['Apple', 'Banana', 'Orange']
grocery_list = vegetables + fruits
print(grocery_list)