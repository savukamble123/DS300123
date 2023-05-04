# Q.8 Count subtress that sum up to a given value x in a binary tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def count_subtrees_with_sum_x(root, x):
    count = 0
    
    def traverse(node):
        nonlocal count
        
        if not node:
            return 0
        
        left_sum = traverse(node.left)
        right_sum = traverse(node.right)
        total_sum = node.val + left_sum + right_sum
        
        if total_sum == x:
            count += 1
        
        return total_sum
    
    traverse(root)
    return count

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(1)
root.left.left = TreeNode(-2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(-1)
root.right.right = TreeNode(2)

x = 6

count = count_subtrees_with_sum_x(root, x)

print("Number of subtrees with sum", x, ":", count)