from collections import deque
from os import listdir
from os.path import join, isfile

def print_file_names(dir):
  for file in sorted(listdir(dir)):
    path = join(dir, file)
    if isfile(path):
      print(file)
    else:
      print_file_names(path)


print_file_names('/home/remessaonline/projects/grokking-algorithms')
