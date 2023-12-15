"""
Iterating lists
"""

top_cities = ['New York City', 'Los Angeles','Chicago', 'Houston', 'Phoenix']
for city in top_cities:
    print('Current city:', city)


for city_index in range(len(top_cities)): # range 0, 5
    print('Current index:', city_index, 'and City:', top_cities[city_index])
    
print('This is the len result:',len(top_cities))


# sum up numbers in a list

spendings_list = [32.40, 18.50, 23.99, 5.23]
# initialize a variable
sum = 0.0
for each_spending in spendings_list:
    sum += each_spending # sum + spending
    
print(sum)