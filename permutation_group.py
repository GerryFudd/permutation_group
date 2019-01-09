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

  def get_by_name(self, name):
    if self.elements[name]:
      return self.elements[name]
    
    return None

  def get_elements_as_list(self):
    return list(self.elements.values)

  def get_element_names(self):
    print(self.elements.keys())
    return self.elements.keys()
