from collections import deque


def create_graph():
  return {}

def add_node(graph, node):
  if not node in graph:
    graph[node] = []

def add_edge(graph, node1, node2):
  if not node1 in graph:
    add_node(graph, node1)
  if not node2 in graph:
    add_node(graph, node2)
  graph[node1].append(node2)
  graph[node2].append(node1)
    

def check_path(graph, root, target):
  search_queue = deque()
  search_queue += graph[root]
  searched = []
  while search_queue:
    person = search_queue.popleft()
    if not person in searched:
      if (person == target):
        return True
      else:
        search_queue += graph[person]
        searched.append(person)
  return False

def person_is_seller(name):
  return name[-1] == "m"


graph = create_graph()
add_node(graph, "you")
add_node(graph, "alice")
add_node(graph, "bob")
add_node(graph, "claire")
add_node(graph, "tom")
add_node(graph, "johnny")
add_node(graph, "anuj")
add_node(graph, "peggy")
add_edge(graph, "you", "alice")
add_edge(graph, "you", "bob")
add_edge(graph, "you", "claire")
add_edge(graph, "bob", "anuj")
add_edge(graph, "bob", "peggy")
add_edge(graph, "alice", "tom")
add_edge(graph, "alice", "johnny")
add_edge(graph, "claire", "peggy")

print(graph)
print(check_path(graph, "you", "tom"))