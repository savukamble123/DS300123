from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def countNodesAtLevel(root: TreeNode, level: int) -> int:
    if not root:
        return 0
    
    queue = deque()
    queue.append(root)
    currentLevel = 0
    count = 0
    
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            if currentLevel == level:
                count += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        currentLevel += 1
        if currentLevel > level:
            break
    
    return count


#       1
#      / \
#     2   3
#    / \   \
#   4   5   6
#          / \
#         7   8

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.right.right.left = TreeNode(7)
root.right.right.right = TreeNode(8)

print(countNodesAtLevel(root, 3))