class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __repr__(self):
        return self.data

root = Node("root")
branch1 = Node("branch1")
branch2 = Node("branch2")
branch3 = Node("branch3")
root.children = [branch1, branch2, branch3]
leaf1 = Node("leaf1")
leaf2 = Node("leaf2")
branch1.children = [leaf1, leaf2]
leaf3 = Node("leaf3")
leaf4 = Node("leaf4")
leaf5 = Node("leaf5")
branch2.children = [leaf3, leaf4, leaf5]
leaf6 = Node("leaf6")
branch3.children = [leaf6]

def printTree(node, deep=0, last=False):
    if deep > 0:
        print("┃ " * int(deep-1), end="")
        if last: print("┗━", end="")
        else: print("┣━", end="")
    if node.children:
      print(f"┓ {node.data}")
      for item in node.children[:-1]:
          printTree(item, deep + 1)
      printTree(node.children[-1], deep + 1, last=True)
    else:
       print(f"╸ {node.data}")

printTree(root)