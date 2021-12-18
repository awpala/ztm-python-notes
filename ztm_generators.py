from modules.ztm_generators_functions import *

# N.B. generators (e.g., `range()`) are a subset of interables (e.g., lists, tuples, strings, etc.)

max_num = 3 * 10**5


# custom generators
g = generator_func(max_num)
is_printed = False # set to `True` to output to console

for num in range(max_num):
  if is_printed:
    print(num, end=', ')

if is_printed:
  print('\n')


# performance comparison
long_time(max_num)
short_time(max_num)
print()


# generators "mocks"
special_for([1, 2, 3])
print()

el_per_line = 10
for i in SpecialRange(last=100):
  print(i, end='\t')
  if not(i % el_per_line):
    print()
print('\n')


# challenge: Fibonacci numbers
max_n = 40
el_per_line = 5
for n, fn in enumerate(fib(max_n)):
  print(f'({n}: {fn})', end='\t\t\t' if n <= 10 else '\t\t')
  if not(n % el_per_line):
    print()
print()

'EOF'
