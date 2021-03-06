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



    
def lca_tuple(root, node1, node2):
    if not root:
        return (None, 0)
    
    left = lca_tuple(root.left, node1, node2)
    right = lca_tuple(root.right, node1, node2)
    
    if root is node1 or root is node2:
        return (root, 1 + left[1] + right[1])

    if left[1] == 1 and right[1] == 1:
        return (root, 2)

    if left[1] > 0:
        return left
    elif right[1] > 0:
        return right
    
    return (None, 0)

def lca_of_3(root, node1, node2, node3):
    if not root:
        return (None, 0)
    
    left = lca_of_3(root.left, node1, node2, node3)
    right = lca_of_3(root.right, node1, node2, node3)
    
    if root is node1 or root is node2 or root is node3:
        return (root, 1 + left[1] + right[1])

    if left[1] == 1 and right[1] == 1:
        return (root, 2)

    if left[1] > 0:
        return left
    elif right[1] > 0:
        return right
    
    return (None, 0)





"""
- Given a binary tree: 

                     10
                    /  \
                  5     12
                 / \    / \   
                3   6  11  13
"""
    
# Test Cases
tree1 = TreeNode(10, 
                 TreeNode(5, 
                          TreeNode(3), 
                          TreeNode(6)), 
                 TreeNode(12, 
                          TreeNode(11), 
                          TreeNode(13)))

print('---LCA of 2 nodes---\n')
print(lca_tuple(tree1, tree1.left.left, tree1.left.right)[0].value, 'expect 5')
print(lca_tuple(tree1, tree1.left, tree1.left.right)[0].value, 'expect 5')
print(lca_tuple(tree1, tree1.left, tree1.right.left)[0].value, 'expect 10')


print('---LCA of 3 nodes---\n')
# print(lca_3(tree1, tree1.left, tree1.left.right, tree1.left.left))
print(lca_of_3(tree1, tree1.left.left, tree1.left.right, tree1.right)[0].value, 'expect 10')
print(lca_of_3(tree1, tree1.left, tree1.left.right, tree1.left.left)[0].value, 'expect 5')
print(lca_of_3(tree1, tree1.left, tree1.right.left, tree1.right.right)[0].value, 'expect 10')



def printTreeByLevelRecur(root):
    result = []
    def helper(nodes):
        if not nodes:
            return
        next_level_nodes = []
        cur_level = []
        while nodes:
            cur = nodes.pop(0)
            cur_level.append(cur.value)
            if cur.left:
                next_level_nodes.append(cur.left)
            if cur.right:
                next_level_nodes.append(cur.right)
        result.append(cur_level)
        helper(next_level_nodes)
    
    helper([root])
    return result

tree1 = TreeNode(10, 
                 TreeNode(5, 
                          TreeNode(3), 
                          TreeNode(6)), 
                 TreeNode(12, 
                          TreeNode(11), 
                          TreeNode(13)))

print('--- Print tree by level recursively ---')
print(printTreeByLevelRecur(tree1))



def printEveryOtherLevel(root):
    if not root:
        return []
    queue = [root]
    level = 0
    result = []
    while queue:
        curLevel = []
        for i in range(len(queue)):
            cur = queue.pop(0)
            if level % 2 == 0:
                curLevel.append(cur.value)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        level += 1
        if curLevel:
            result.append(curLevel)
    
    return result

tree1 = TreeNode(10, 
                 TreeNode(5, 
                          TreeNode(3), 
                          TreeNode(6)), 
                 TreeNode(12, 
                          TreeNode(11), 
                          TreeNode(13)))

print('--- Print tree - every other level ---')
print(printEveryOtherLevel(tree1))



def isSubtree(self, root, subRoot) -> bool:
    '''Check if subRoot is a subtree of root
    '''
    def isSameTree(r, s):
        if not r and not s:
            return True
        if r and s:
            return r.val == s.val and isSameTree(r.left, s.left) and isSameTree(r.right, s.right)
        
    if not root:
        return False

    return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)