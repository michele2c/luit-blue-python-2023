"""
Loops - break and continue
"""

# ----- WHILE loop ---------
# counter = 1
# while counter < 11:
#     print(counter)
#     counter += 1 # increment by 1
# print('Done!')


# # use ''' triple quotes to use multi-line strings
# print('''
#     ======================
#     THE SECRET NUMBER GAME
#     ======================
#     ''')
# secret_number = 8
# user_input = int(input('Try to guess the secret number from 0 to 10: '))
# while user_input != secret_number:
#     print('Wrong!')
#     user_input = int(input('Try to guess the secret number from 0 to 10: '))
# print('Perfect!')


# ======= FOR loop =============

# # for loop will loop for every letter of the word hello
# for letter in 'hello':
#     print('Current letter: ', letter)
    
    
# for counter in range(1,11):
#     print(counter)
# print('Done!')


# for counter in range(1,11,2):
#     print(counter)
# print('Done!')


# ======= BREAK and CONTINUE =============
# while True:
#     name = input('Enter a name or EXIT to close the program: ')
#     if (name == 'EXIT'):
#         break
#     print('Hello, ', name)


# # Continue is also typically used with if statements when we sometimes want to
# # skip a certain iteration

# for i in range(1, 21):
#     if i % 5 == 0: # if number is divisible by 5 
#         continue # continue the loop and don't print the number
#     print(i)
    
    
# ======== PASS ================
# for i in range(11):
#     pass

# ======== NESTED LOOP ==========
for a in range(1,4):
    for b in range(1,4):
        print(a,'x', b, '=', a*b)
    print(9*'-')
        