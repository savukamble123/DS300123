# Q.9 Find maximum level sum in Binary Tree
class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def max_level_sum(root):
    if root is None:
        return 0
        
    level_sum = 0
    max_sum = float('-inf')
    q = [root]
    
    while q:
        level_size = len(q)
        level_sum = 0
        
        for i in range(level_size):
            node = q.pop(0)
            level_sum += node.val
            
            if node.left:
                q.append(node.left)
                
            if node.right:
                q.append(node.right)
                
        max_sum = max(max_sum, level_sum)
        
    return max_sum

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(max_level_sum(root))