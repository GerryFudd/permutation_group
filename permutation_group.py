import helpers

@helpers.memoize
def make_permutation_set(set_size):
  if set_size <= 1:
    return list(map(Permutation, [[0]]))

  if set_size == 2:
    return list(map(Permutation, [[0, 1], [1, 0]]))
  
  result = []
  previous_permutation_set = make_permutation_set(set_size - 1)
  first_element = 0
  while first_element < set_size:
    tail = []
    while len(tail) < set_size - 1:
      if len(tail) < first_element:
        tail.append(len(tail))
      else:
        tail.append(len(tail) + 1)

    for permutation in previous_permutation_set:
      permuted_tail = permutation.apply(tail)
      result.append(Permutation([first_element] + permuted_tail))
    first_element += 1
  return result

class Permutation:
  name = None

  def __init__(self, perm):
    self.perm = perm

  def set_name(self, name):
    self.name = name

  def apply(self, permutation):
    result = []
    for value in self.perm:
      result.append(permutation[self.perm[len(result)]])
    return result

class PermutationGroup:
  def __init__(self, set_size):
    self.elements = {}
    values = make_permutation_set(set_size)
    name = 'e'
    for permutation in values:
      permutation.set_name(name)
      self.elements[name] = permutation
      name = helpers.get_next_char(name)
    self.table = self.__make_multiplication_table()

  def get_by_name(self, name):
    if self.elements[name]:
      return self.elements[name]
  
  def get_elements_as_list(self):
    return self.elements.values()
  
  def get_by_value(self, perm):
    for element in self.get_elements_as_list():
      if element.perm == perm:
        return element

  def get_element_names(self):
    return self.elements.keys()

  def __multiply(self, a, b):
    return self.get_by_value(self.get_by_name(a).apply(self.get_by_name(b).perm))

  def __make_multiplication_table(self):
    table = {}
    for a in self.get_elements_as_list():
      for b in self.get_elements_as_list():
        table[helpers.hash_pair(a.name, b.name)] = self.__multiply(a.name, b.name)
    
    return table

  def multiply(self, a, b):
    return self.table[helpers.hash_pair(a, b)]
  
  def display_table(self):
    table_string = ' '
    for name in self.get_element_names():
      table_string += ' ' + name
    
    table_string += '\n'
    for multiplier in self.get_element_names():
      table_string += multiplier
      for multiplicand in self.get_element_names():
        table_string += ' ' + self.multiply(multiplier, multiplicand).name
      
      table_string += '\n'

    return table_string
