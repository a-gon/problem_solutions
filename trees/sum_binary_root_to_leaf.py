class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.result = 0
        
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.dfs(root, 0)
        return self.result
        
        
    def dfs(self, root, cur_num):
        if root: 
            cur_num = (cur_num << 1) | root.val
            self.dfs(root.left, cur_num)
            self.dfs(root.right, cur_num)
            if not root.left and not root.right:
                self.result += cur_num