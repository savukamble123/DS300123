# Q.6 Find sum of all left leaves in a given Binary Tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sum_of_left_leaves(root):
    if root is None:
        return 0
    else:
        sum = 0
        if root.left is not None and root.left.left is None and root.left.right is None:
            sum += root.left.val
        sum += sum_of_left_leaves(root.left)
        sum += sum_of_left_leaves(root.right)
        return sum

root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(25)
root.left.left = Node(3)
root.left.right = Node(8)
root.left.right.left = Node(6)
root.left.right.right = Node(9)

print("Sum of all left leaves:", sum_of_left_leaves(root)) 
