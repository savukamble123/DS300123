# Q.2 Find height of a given tree.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)

        return max(left_height, right_height) + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Height of the binary tree is:", height(root)) 