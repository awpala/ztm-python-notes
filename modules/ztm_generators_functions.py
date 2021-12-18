from .ztm_decorators_functions import performance

# custom generators
def generator_func(num: int) -> int:
  for i in range(num):
    yield i # each successive iteration of `next()` increments `i` until `num` is reached, beyond which `StopIteration` exception is thrown


# performance comparison
@performance
def short_time(num: int) -> None:
  for i in range(num):       # generator only
    i*5

@performance
def long_time(num: int) -> None:
  for i in list(range(num)): # stores in memory via `list()`
    i*5


# generators "mocks"
def special_for(iterable):
  '''
  a demonstration of a `for-in` style loop over an iterable object
  '''
  iterator = iter(iterable)
  while True:
    try:
      val = next(iterator)
      print(iterator, f'value: {val}', sep=', ') # same iterator object used for each iteration
    except StopIteration:
      print('generator exhausted')
      break

class SpecialRange:
  current = 0

  def __init__(self, first: int = 0, last: int = 1):
    self.first = first
    self.last = last

  def __iter__(self):
    return self

  def __next__(self):
    if SpecialRange.current < self.last:
      num = SpecialRange.current
      SpecialRange.current += 1
      return num
    raise StopIteration # iterator is exhausted once `self.current`` exceeds `self.last`


# challenge: Fibonacci numbers
def fib(num: int) -> int:
  f0, f1 = 0, 1
  a, b = f0, f1
  for _ in range(num):
    yield a
    temp = a
    a = b
    b += temp

