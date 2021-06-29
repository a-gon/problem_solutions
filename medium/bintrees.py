class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


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

from collections import deque
def levelOrder(root):
    ''' 
    Level order traversal of a tree
    '''
    queue = deque([root,])
    result = []
    while len(queue):
        level = []
        for i in range(len(queue)):
            node = queue.popleft()
            level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


def levelOrder_recur(root):
    levels = []
    if not root:
        return levels

    def helper(node, level):
        if len(levels) == level:
            levels.append([])
        levels[level].append(node.value)
        if node.left:
            helper(node.left, level + 1)
        if node.right:
            helper(node.right, level + 1)
        
    helper(root, 0)
    return levels


tree1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print(levelOrder(tree1), 'expected [[1], [2, 3], [4, 5, 6, 7]]')
print(levelOrder_recur(tree1), 'expected [[1], [2, 3], [4, 5, 6, 7]]')

        

