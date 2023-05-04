# Q.3 Perform Pre-order, Post-order, In-order traversal
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def print_inorder(node):
    if node:
        print_inorder(node.left)
        print(node.value)
        print_inorder(node.right)

def print_preorder(node):
    if node:
        print(node.value)
        print_preorder(node.left)
        print_preorder(node.right)

def print_postorder(node):
    if node:
        print_postorder(node.left)
        print_postorder(node.right)
        print(node.value)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# In-order traversal: 4 2 5 1 6 3 7
print("In-order traversal:")
print_inorder(root)

# Pre-order traversal: 1 2 4 5 3 6 7
print("Pre-order traversal:")
print_preorder(root)

# Post-order traversal: 4 5 2 6 7 3 1
print("Post-order traversal:")
print_postorder(root)