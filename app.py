def memoize(f):
  cache = {}
  def memoized_function(*args):
    if hash(args) in cache:
      return cache[hash(args)]
    result = f(*args)
    cache[hash(args)] = result
    return result

  return memoized_function

@memoize
def factorial(num):
  if num <= 1:
    return 1
  return num * factorial(num - 1)

class Permutation:
  def __init__(self, perm):
    self.perm = perm

  def apply(self, permutation):
    result = []
    for value in self.perm:
      result.append(permutation[self.perm[len(result)]])
    return result

@memoize
def make_permutation_set(set_size):
  if set_size <= 1:
    return map(Permutation, [[0]])

  if set_size == 2:
    return map(Permutation, [[0, 1], [1, 0]])
  
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

class PermutationGroup:
  def __init__(self, set_size):
    self.size = factorial(set_size)

set_size = input("How many elements are in the underlying set?\n> ")
permutation_group = PermutationGroup(set_size)

print('There are {0} elements in this permutation group.'.format(permutation_group.size))

def get_list(permutation):
  return permutation.perm

print('The permutation set is:\n{0}'.format(map(get_list, make_permutation_set(set_size))))
