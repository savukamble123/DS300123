# Q.3 Function to print all the leaves in a given binary tree.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_leaves(root):
    if root is None:
        return
    
    if root.left is None and root.right is None:
        print(root.val)
    
    if root.left is not None:
        print_leaves(root.left)
    
    if root.right is not None:
        print_leaves(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print_leaves(root)