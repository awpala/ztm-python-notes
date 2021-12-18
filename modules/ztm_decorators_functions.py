from typing import Callable, Tuple, Dict
from time import time

# higher order functions (HOCs)
def greet(func: Callable) -> None:
  func() # calls another function

def greet2() -> Callable:
  def func() -> int:
    return 5
  return func # returns another function


# custom decorator demo
def my_decorator(func: Callable) -> Callable:
  def wrap_func(*args: Tuple[str], **kwargs: Dict[str, str]) -> None:
    line_separator = '*' * 10
    print(line_separator)
    func(*args, **kwargs)
    print(line_separator)
  return wrap_func

def hello(*names: str, emoji: Dict[str, str] = ':)') -> None:
  addressees = ', '.join(names)
  print(f'hello {addressees} {emoji}')

@my_decorator
def hello_decorated(*names: str, emoji: Dict[str, str] = ':)') -> None:
  hello(*names, emoji=emoji)

# performance decorator
def performance(func: Callable) -> None:
  def wrapper(*args, **kwargs):
    S_PER_MS = 1000
    time_start = time()
    result = func(*args, **kwargs)
    time_to_run = (time() - time_start)*S_PER_MS
    print(f'{func.__name__}() ran in {time_to_run} ms')
    return result
  return wrapper

@performance
def long_time() -> None:
  for i in range(10**7):
    i*5
