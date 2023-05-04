# Q.7 Find sum of all nodes of the given perfect binary tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
 
 
def perfect_tree_sum(root):
    """
    Function to find the sum of all nodes in a perfect binary tree
    """
    if not root:
        return 0
     
    height = 0
    temp = root
    while temp:
        height += 1
        temp = temp.left
     
    nodes = 2 ** height - 1
    return nodes * root.val
 

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)
 
print("Sum of all nodes in the perfect binary tree:", perfect_tree_sum(root))