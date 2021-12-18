from modules.ztm_error_handling_functions import *


# error handling via `try`` block
while True:
  try:
    age = int(input('What is your age? ')) # string or alphanumeric input generates ValueError 
  except ValueError:
    print('please enter a number')
    continue
  else:          # no error 
    print('input received without error!'); print()
    break # exits `while` loop after appropriate input received
  finally:       # reached after EACH `try`, regardless of `except` or `else`
    pass # add logging, cleanup, etc.


# generating exceptions via functions
sum_func('1', 2) # TypeError
div_func('1', 2) # TypeError
div_func(1, 0)   # ZeroDivisionError
print()


# throwing exceptions
try:
  raise Exception('cut it out!')
except Exception as err:
  print(err)

'EOF'
