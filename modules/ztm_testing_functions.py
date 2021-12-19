def do_stuff(num: int = 0) -> int:
  try:
    return num + 5
  except TypeError as err:
    return err
