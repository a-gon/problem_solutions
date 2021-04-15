class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.result = []
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        self.result.append([root.val])
        
        self.bfs([root.left, root.right])
        
        return self.result
    
    def bfs(self, nodes):
        if not nodes:
            return
        level_vals, next_level = [], []
        for n in nodes:
            if n:
                level_vals.append(n.val)
                next_level.append(n.left)
                next_level.append(n.right)
        if level_vals:
            self.result.append(level_vals)
        self.bfs(next_level)