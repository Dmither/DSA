# як виключити з обходу вузли, які не ведуть до цілі?

def find_lowest_cost_node(costs, processed):
  lowest_cost = float("inf")
  lowest_cost_node = None
  for node in costs:
    cost = costs[node]
    if cost < lowest_cost and node not in processed:
      lowest_cost = cost
      lowest_cost_node = node
  return lowest_cost_node


def find_lowest_path(graph, start, fin):
  queue = []
  costs = {}
  parents = {}
  for node in graph[start]:
    costs[node] = graph[start][node]
    parents[node] = start
    queue.append(str(node))
  while len(queue) > 0:
    x = queue.pop(0)
    for node in graph[x]:
      if node not in costs:
        costs[node] = float("inf")
        parents[node] = None
        queue.append(str(node))
  print(costs)
  print(parents)

  processed = []

  node = find_lowest_cost_node(costs, processed)
  while node is not None:
    cost = costs[node]
    neigbors = graph[node]
    for n in neigbors.keys():
      new_cost = cost + neigbors[n]
      if new_cost < costs[n]:
        costs[n] = new_cost
        parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs, processed)
  
  parent = parents[fin]
  path = [fin]
  while parent != start:
    path = [parent] + path
    parent = parents[parent]
  path = [start] + path

  print(costs)
  print(parents)

  return [path, costs[fin]]


graph = {}

graph["s"] = {}
graph["a"] = {}
graph["b"] = {}
graph["c"] = {}
graph["d"] = {}
graph["e"] = {}
graph["f"] = {}

graph["s"]["a"] = 5
graph["s"]["b"] = 2

graph["a"]["c"] = 4
graph["a"]["d"] = 2

graph["b"]["a"] = 8
graph["b"]["d"] = 7
graph["b"]["e"] = 2

graph["c"]["f"] = 3

graph["d"]["f"] = 1

print(graph)

[path, cost] = find_lowest_path(graph, "s", "f")

print(path)
print(cost)