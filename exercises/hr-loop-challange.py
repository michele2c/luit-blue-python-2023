# Hancker Rank challenge
n = int(input())

numbers =[]
for i in range(n):
    if i < n:
        num = i**2
        numbers.append(num)

print(*numbers, sep = '\n')


a = [1, 2, 3, 4, 5]

# printing the list using * operator separated by comma 
print(*a)

# printing the list using * and sep operator
print("printing lists separated by commas")

print(*a, sep = ", ") 

# print in new line
print("printing lists in new line")

print(*a, sep = "\n")