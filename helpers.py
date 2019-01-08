def memoize(f):
  cache = {}
  def memoized_function(*args):
    if hash(args) in cache:
      return cache[hash(args)]
    result = f(*args)
    cache[hash(args)] = result
    return result

  return memoized_function

def get_next_char(char):
  if char is 'e':
    return 'a'
  
  if char is 'd':
    return 'f'
  
  if char is 'n':
    return 'p'

  if char is 'z':
    return 'A'
  
  if char is 'Z':
    return u'\u03b1'
  
  # if isinstance(char, unicode):
  #   print(char)
  #   return unichr(ord(char) + 1)

  return chr(ord(char) + 1)
