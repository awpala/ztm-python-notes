import random as rand
from random import random, randint, choice, shuffle
from sys import argv
from collections import Counter, defaultdict, OrderedDict
import datetime
from array import array

# N.B. complete built-in modules reference: https://docs.python.org/3/py-modindex.html
# third-party packages repo for pip (cf. Node.js npm, Ruby gem, etc.): https://pypi.org/


# random
row_items = 5
for i, prop in enumerate(dir(rand)):
  print(prop, end='\t\t')
  if not(i % row_items) and i > 0:
    print()
print()

rand_n = random()
rand_int = randint(1, 10)

choices = [1, 2, 3, 4, 5]
rand_choice = choice(choices)
shuffle(choices) # N.B. `shuffle()` modifieds in-place
print()


# sys
print(argv) # command-line arguments
filepath = argv[0]
# N.B. additional command-line args (if provided) are in argv[1], argv[2], etc.


# specialized data types
li = [1, 2, 3, 4, 5, 6, 7, 7]
sentence = 'blah blah blah thiking about python'
counts_numbers = Counter(li)
counts_chars = Counter(sentence)

default_dict = defaultdict(lambda: 'non-existent key', {'a': 1, 'b': 2})
non_existent_key = default_dict['c']
valid_key = default_dict['a']

ordered_dict1 = OrderedDict()
ordered_dict1['a'] = 1
ordered_dict1['b'] = 2
ordered_dict2 = OrderedDict()
ordered_dict2['b'] = 2
ordered_dict2['a'] = 1
are_equal_dicts = ordered_dict1 == ordered_dict2 # False - keys' insertion is order-dependent in `OrderedDict`
# N.B. As of Python 3.7, `dict` objects insert keys in order by default (reference: https://softwaremaniacs.org/blog/2020/02/05/dicts-ordered/en/)


# datetime
time = datetime.time(5, 2, 3).__str__()
today = datetime.date.today().__str__()


# array
arr = array('i', [1, 2, 3])
first_el = arr[0]


'EOF'
