# Q.10 Print the nodes at odd levels of a tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_odd_level(root):
    if not root:
        return
    queue = [root]
    level = 1
    while queue:
        size = len(queue)
        for i in range(size):
            curr_node = queue.pop(0)
            if level % 2 != 0:
                print(curr_node.val, end=" ")
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        level += 1



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Nodes at odd levels:")
print_odd_level(root) 