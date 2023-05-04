# Q.5 Implement BFS (Breath First Search) and DFS (Depth First Search)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
 
def BFS(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while queue:
        curr_node = queue.pop(0)
        print(curr_node.val, end=' ')
        if curr_node.left is not None:
            queue.append(curr_node.left)
        if curr_node.right is not None:
            queue.append(curr_node.right)
 
# DFS implementation using recursion
def DFS(root):
    if root is None:
        return
    print(root.val, end=' ')
    DFS(root.left)
    DFS(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("BFS traversal:")
BFS(root)
print("\nDFS traversal:")
DFS(root)