import permutation_group

set_size = input("How many elements are in the underlying set?\n> ")
group = permutation_group.PermutationGroup(int(set_size, 10))

print('There are {0} elements in this permutation group.'.format(len(group.elements)))

names_message = 'The element names are: '
names_list = []
name_index = 0
for name in group.get_element_names():
  names_message += '{' + str(name_index) + '} '
  names_list.append(name)
  name_index += 1
print(names_message.format(*names_list))

def multiply():
  nameA = input("Let's multiply two elements.\nChoose a multiplier.\n> ")
  a = group.get_by_name(nameA)
  print('{0} = {1}'.format(a.name, a.perm))
  nameB = input("Choose a multiplicand.\n> ")
  b = group.get_by_name(nameB)
  print('{0} = {1}'.format(b.name, b.perm))
  product = group.multiply(a.name, b.name)
  print('{0}{1} = {2} = {3}'.format(a.name, b.name, product.name, product.perm))

option = ''
while option != 'leave':
  option = input("What would you like to do?\n(multiply, view, leave)> ")
  if option == 'multiply':
    multiply()
  elif option == 'view':
    print(group.display_table())
  elif option != 'leave':
    print('"{0}" is not a valid option.'.format(option))


