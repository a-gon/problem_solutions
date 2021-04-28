from TreeNode import TreeNode

def isUnivalTree(root: TreeNode) -> bool:
    return recurse(root, root.val)

def recurse(root, val):
    if not root:
        return True
    if root.val != val:
        return False
    else:
        return recurse(root.left, root.val) and recurse(root.right, root.val)