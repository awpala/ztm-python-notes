def sum_func(num1: int, num2: int) -> int:
  try:
    return num1 + num2
  except TypeError as err:
    print(f'please provide two integers as arguments: {err}')


def div_func(num1: int, num2: int) -> int:
  try:
    return num1 / num2
  except (TypeError, ZeroDivisionError) as err:
    print(err)
