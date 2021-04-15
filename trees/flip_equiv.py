class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is root2:
            return True
        if not root1 or not root2 or root1.val != root2.val: 
            return False
        # print(f'root1: {root1.val}, root2: {root2.val}' )

        return (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left) \
            or self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right))

# time complexity: O(N) where N is min(num of tree1 and tree2 nodes)
# space complexity: O(H) where H is min(height of tree1 and tree2)