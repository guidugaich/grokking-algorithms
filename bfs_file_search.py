from collections import deque
from os import listdir
from os.path import join, isfile

def print_file_names(start_dir):
  search_queue = deque()
  search_queue.append(start_dir)
  while search_queue:
    print('search_queue', search_queue)
    dir = search_queue.popleft() 
    for file in sorted(listdir(dir)):
      path = join(dir, file)
      if isfile(path):
        print(file)
      else:
        search_queue.append(path)

def print_file_names_recursive(dir):
  for file in sorted(listdir(dir)):
    path = join(dir, file)
    if isfile(path):
      print(file)
    else:
      print_file_names_recursive(path)



print_file_names('/home/remessaonline/projects/grokking-algorithms')
