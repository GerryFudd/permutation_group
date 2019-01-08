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

selected_element = input("Which element would you like to see?\n> ")
print(group.get_by_name(selected_element).perm)
