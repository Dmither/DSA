# An individual node in a Binary Tree
class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.value)


class BinaryTree(Node):
    pass


class BinarySearchTree(Node):
    def __init__(self, data=None):
        self.root = None
        if data:
            self.root  = Node(data.pop(0))
            for item in data:
                node = self.root
                while True:
                    if item == node.value: break
                    elif item < node.value:
                        if node.left:
                            node = node.left
                            continue
                        node.left = Node(item)
                        break
                    else:
                        if node.right:
                            node = node.right
                            continue
                        node.right = Node(item)
                        break
    def __repr__(self):
        return str(self.root)
                    
                    
tree = BinarySearchTree([4, 2, 8, 1, 3, 6, 10, 7, 9, 5])
print(tree.root.left.left)
print(tree.root.left)
print(tree.root.left.right)
print(tree)
print(tree.root.right.left.left)
print(tree.root.right.left)
print(tree.root.right.left.right)
print(tree.root.right)
print(tree.root.right.right.left)
print(tree.root.right.right)


