class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def mps(root) -> int:
    def helper(root):
        nonlocal max_path
        if not root:
            return 0
        
        left = helper(root.left)
        right = helper(root.right)
        cur_path = root.value + left + right
        max_path = max(max_path, cur_path)
        
        return max(0, root.value + left, root.value + right)
        
    max_path = -float('inf')
    helper(root)
    return max_path

tree = TreeNode(1, TreeNode(-10, TreeNode(3, TreeNode(5, TreeNode(13), TreeNode(-1)), TreeNode(-1))), TreeNode(-5, TreeNode(-20), TreeNode(-21)))

print(mps(tree), 'expected 21')