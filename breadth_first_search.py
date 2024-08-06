from collections import deque

def person_is_seller(person):
  return person[-1] == 'm'

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "johnny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["johnny"] = []

def breadth_first_search(name):
  search_queue = deque()
  search_queue += graph[name]
  already_searched = set()

  while search_queue:
    print('search_queue', search_queue)
    print('already_searched', already_searched)
    person = search_queue.popleft()
    if person not in already_searched:
      if person_is_seller(person):
        print(person, 'is a mango seller')
        return True
      else:
        search_queue += graph[person]
        already_searched.add(person)
  return False

print(breadth_first_search("you"))
