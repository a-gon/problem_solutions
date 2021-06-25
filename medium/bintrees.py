def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    ''' 
    cases:
    1. not L and not R >> return none
    2. root == to p or q >> return root
    3. L and R >> return root
    4. L or R >> return L or R wichever is not none
    
    '''
    if not root:
        return None

    if root == p or root == q:
        return root
    
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    
    if left and right:
        return root
    
    return left or right