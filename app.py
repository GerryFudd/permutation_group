import permutation_group

set_size = input("How many elements are in the underlying set?\n> ")
group = permutation_group.PermutationGroup(set_size)

print('There are {0} elements in this permutation group.'.format(len(group.elements)))

print('The permutation set is:\n{0}'.format(group.get_elements_as_list()))
print('The element names are:')
for name in group.get_element_names():
  print(name)
