import re
from modules.ztm_regex_functions import validate_email, validate_password

# simple pattern matching
search_string = 'search this inside of this text please!'

has_word = 'this' in search_string # a valid (but limited) approach

pattern = re.compile('this')

match_obj = pattern.search(search_string) # a more general approach
match_span = match_obj.span()
match_start = match_obj.start()
match_end = match_obj.end()
match_group = match_obj.group()

match_obj_all = pattern.findall(search_string)

# complex pattern matching
pattern_comp = re.compile(r'([a-zA-Z]).([a])')
search_string_comp = 'hey, how are you!?'

match_obj_comp = pattern_comp.search(search_string_comp)
match_group_comp = match_obj_comp.group()

match_obj_all_comp = pattern_comp.findall(search_string_comp)


# example: email validator
valid_email = 'test@test.com'
invalid_email = 'test!invalid'

is_valid_email = validate_email(valid_email)
is_invalid_email = not validate_email(invalid_email)

while True:
  user_email_input = input('Enter an email: ')
  is_valid_email = validate_email(user_email_input)
  if is_valid_email:
    print('valid email entered, now exiting...')
    break
  else:
    print('invalid email, try again...')
print()


# challenge: password validator
while True:
  user_password_input = input('Enter a password: ')
  is_valid_password = validate_password(user_password_input)
  if is_valid_password:
    print('valid password entered, now exiting...')
    break
  else:
    print('invalid password, try again...')


# reference regex builder tool: https://regex101.com/
# reference regex lessons: https://regexone.com/


'EOF'
