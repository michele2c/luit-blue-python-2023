#list checking presence

for char in 'happy message':
  print(char)

guest_list = ['maria', 'pedro', 'joao', 'paulo', 'madalena']
name = str.lower(input(('Qual seu nome? ')))
if name in guest_list:
  print('Welcome!', name)
else:
  print('Voce nao esta na lista')

# # use this example tp make a list for departments for the project
# dep_names = ['marketing', 'accounting', 'finops']
# dep_name = str.lower(input('Department: '))
# if dep_name not in dep_names:
#   print('Ooops... Your department cannot use this tool.')
# # else:
#call function