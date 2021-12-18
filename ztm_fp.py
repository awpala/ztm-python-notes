from modules.ztm_fp_functions import *
from functools import reduce

old_list = [1, 2, 3]
list_one = [1, 2, 3]
list_two = [10, 20, 30]
a_tuple = ('a', 'b', 'c')

# pure functions
new_list = multiply_by_two_raw(old_list)


# map, filter, zip, reduce
mapped_list = list(map(multiply_by_two, old_list)) # `map()` is a pure function -- `old_list` remains unmodified

filtered_list = list(filter(only_odd, old_list))

zipped_list = list(zip(list_one, list_two))
zipped_pair = list(zip(list_one, a_tuple))
zipped_triplet = list(zip(list_one, list_two, a_tuple))

total = reduce(accumulator, new_list, 0)


# lambda expressions
mapped_list = list(map(lambda item: item * 2, old_list))
filtered_list = list(filter(lambda item: bool(item % 2), old_list))
total = reduce(lambda acc, item: acc + item, new_list, 0)


# challenge: sort a list of tuples by second element
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
sorted_a = sorted(a, key=lambda x: x[1])


# comprehensions - list, set, dict
list_of_chars = [char for char in 'hello']
list_of_nums = [num for num in range(100)]
list_of_nums_doubled = [num * 2 for num in range(100)]
list_of_nums_filtered_evens = [num**2 for num in range(100) if not(num % 2)]

set_of_chars = {char for char in 'hello'}
set_of_nums_filtered_evens = {num**2 for num in range(100) if not(num % 2)}

dict1 = {k: v**2 for k, v in {'a': 1, 'b': 2}.items()}
dict2 = {k: v**2 for k, v in zip(list_one, list_two) if not(k % 2)}
dict3 = {num: num*2 for num in [1, 2, 3]}


# challenge: find duplicates
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list(set([char for char in some_list if some_list.count(char) > 1]))

'EOF'
