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

def maxLevelSum(root):
    if not root:
        return None
    queue = deque([root,])
    max_sum = -float('inf')
    while queue:
        level_sum = 0
        for i in range(len(queue)):
            node = queue.popleft()
            level_sum += node.value
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        max_sum = max(max_sum, level_sum)
    return max_sum
tree1 = TreeNode(1, TreeNode(20, TreeNode(4), TreeNode(5)), TreeNode(13, TreeNode(6), TreeNode(7)))

print(maxLevelSum(tree1), 'expect 33')
print(maxLevelSum(None), 'expect None')
print(maxLevelSum(TreeNode(1)), 'expect 1')

def isSymmetric(root):
    
    def helper(root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        return (root1.value == root2.value) and helper(root1.left, root2.right) and helper(root1.right, root2.left)
        
    if not root:
        return True

    return helper(root.left, root.right)

print('Checking if tree is symmetric: ')
tree1 = TreeNode(1, TreeNode(20, TreeNode(4), TreeNode(5)), TreeNode(13, TreeNode(6), TreeNode(-1)))
print(isSymmetric(tree1), 'expected False')
tree1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(2, TreeNode(5), TreeNode(4)))
print(isSymmetric(tree1), 'expected True')



def findMin(root):
    if not root:
        return float('inf')
    cur_min = root.value
    min_left = min(cur_min, findMin(root.left))
    min_right = min(cur_min, findMin(root.right))

    return min(cur_min, min_left, min_right)

tree1 = TreeNode(1, TreeNode(20, TreeNode(4), TreeNode(5)), TreeNode(13, TreeNode(6), TreeNode(-1)))

print(findMin(tree1))


def findAvgEachLevel(root):
    if not root:
        return None
    queue = deque([root,])
    result = []
    while queue:
        level = []
        for i in range(len(queue)):
            node = queue.popleft()
            level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(sum(level) / len(level))
    return result

tree1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print(findAvgEachLevel(tree1))

def countEvenNodes(root):
    if not root:
        return 0
    
    return (root.value % 2 == 0) + countEvenNodes(root.left) + countEvenNodes(root.right)

tree1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print(countEvenNodes(tree1), 'expected 3')


def rightLeafSum(root):
    if not root:
        return 0
    cur_sum = 0
    if root.right and not root.right.left and not root.right.right:
        cur_sum += root.right.value
        return cur_sum

    return cur_sum + rightLeafSum(root.left) + rightLeafSum(root.right)

tree1 = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(7)))
print(rightLeafSum(tree1), 'expected 12')
tree1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, None, TreeNode(7))), TreeNode(3, TreeNode(6), TreeNode(7)))
print(rightLeafSum(tree1), 'expected 14')
print(rightLeafSum(None), 'expected 0')



def inOrderTraversal(root):
    ''' 
    Iterative in-order traversal, returns a lst with node values traversed in-order
    '''
    if not root:
        return []
    result = []
    stack = []
    cur = root

    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            result.append(cur.value)
            cur = cur.right

    return result


# tree1:
#          1
#        /   \
#       2     3
#      / \   / \
#     4   5 6   7
#    / \
#   8   9
tree1 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print('---Iterative In-order Traversal---') 
print(inOrderTraversal(tree1), 'expected: [8, 4, 9, 2, 5, 1, 6, 3, 7]')

