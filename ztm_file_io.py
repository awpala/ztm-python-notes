path_to_input_file = './assets/input.txt'
path_to_output_file = './assets/output.txt'


# basic operations
file = open(path_to_input_file, mode='r') # N.B. `'r'` is the default mode for `open()`

read_contents_str = file.read()

file.seek(0) # reset to start position of file
read_content_lines = file.readlines()

file.close()


# file modes
with open(path_to_input_file) as file: # N.B. opens file to position `0` by default
  contents_lines = file.readlines()
# <-- `file` closes automatically here upon executing `with...` context manager

with open(path_to_output_file, mode='w') as file: # mode `'w'` overwrites an existing file, or creates a new file if non-existing
  written_chars_count = file.write('hello world\nprogramming is fun\n')

with open(path_to_output_file, mode='a') as file: # mod `'a'` appends to the end of the file
  written_chars_count = file.write('appending more text here...\n')


# error handling
try:
  with open('invalid path', mode='r') as file:
    print(file.read())
except FileNotFoundError as err:
  print('file does not exist')
  # raise err # re-throw to generate err in terminal (optional)

try:
  with open(path_to_input_file, mode='xaasdfa') as file:
    print(file.read())
except ValueError as err:
  print('invalid mode')
  raise err


# N.B. cf. library `pathlib` for OS-independent file system operations
# (reference: https://docs.python.org/3/library/pathlib.html)


'EOF'
