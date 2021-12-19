import re

# reference email regex pattern: https://emailregex.com
pattern_email = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')

pattern_password = re.compile(r'[A-Za-z0-9$%#@]{7,}[0-9]')


def validate_email(email: str) -> bool:
  return len(pattern_email.findall(email)) == 1


def validate_password(password: str) -> bool:
  '''
  password requirements:
    * at least eight chars long
    * contains any letters, numbers, or symbols in $%#@
    * must end with number
  '''
  return len(pattern_password.findall(password)) == 1

