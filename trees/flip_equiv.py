from TreeNode import TreeNode


def flipEquiv(root1: TreeNode, root2: TreeNode) -> bool:
    if root1 is root2:
        return True
    if not root1 or not root2 or root1.val != root2.val: 
        return False
    # print(f'root1: {root1.val}, root2: {root2.val}' )

    return (flipEquiv(root1.left, root2.right) and flipEquiv(root1.right, root2.left) \
        or flipEquiv(root1.left, root2.left) and flipEquiv(root1.right, root2.right))

# time complexity: O(N) where N is min(num of tree1 and tree2 nodes)
# space complexity: O(H) where H is min(height of tree1 and tree2)