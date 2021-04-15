class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.result = 0
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.dfs(root, None, None)
        
        return self.result
        
        
    def dfs(self, root, p, gp):
        if root:
            if gp and gp.val % 2 == 0:
                self.result += root.val
            self.dfs(root.left, root, p)
            self.dfs(root.right, root, p)