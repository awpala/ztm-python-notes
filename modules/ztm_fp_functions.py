from typing import List

# pure functions
def multiply_by_two_raw(li: List) -> List:
  '''
  A pure function has two properties:
    1. Always returns the same output for the same input
    2. Does not produce any side effects
  '''
  new_list = []
  for item in li:
    new_list.append(item * 2)
  return new_list


# map
def multiply_by_two(item: int) -> int:
  return item * 2


# filter
def only_odd(item: int) -> bool:
  return bool(item % 2)


# reduce
def accumulator(acc: int, item: int) -> int:
  return acc + item

