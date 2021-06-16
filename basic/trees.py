class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        
def countTreeNodesIterative(root: TreeNode) -> int:
    if not root:
        return 0
    stack = [root]
    count = 0
    while stack:
        node = stack.pop()
        if node:
            count += 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
    
    return count

    

def countTreeNodesRecursive(root: TreeNode) -> int:
    if not root:
        return 0
    return countTreeNodesRecursive(root.left) + countTreeNodesRecursive(root.right) + 1

# Test Cases
print('Num nodes, iterative:')
print(countTreeNodesIterative(None)) # 0
print(countTreeNodesIterative(TreeNode(1, TreeNode(2), TreeNode(3)))) # 3
print(countTreeNodesIterative(TreeNode(2, TreeNode(29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9)))))) # 6
print(countTreeNodesIterative(TreeNode())) # 1
print('Num nodes, recursive:')
print(countTreeNodesRecursive(None)) # 0
print(countTreeNodesRecursive(TreeNode(1, TreeNode(2), TreeNode(3)))) # 3
print(countTreeNodesRecursive(TreeNode(2, TreeNode(29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9)))))) # 6
print(countTreeNodesRecursive(TreeNode())) # 1


class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def sumBTIterative(root: TreeNode) -> int:
    if not root:
        return 0
    stack = [root]
    sum = 0
    while stack:
        node = stack.pop()
        if node:
            sum += node.value
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return sum

def sumBTRecursive(root: TreeNode) -> int:
    if not root:
        return 0
    return root.value + sumBTRecursive(root.left) + sumBTRecursive(root.right)

# Test Cases
print("Sum of all nodes in BT: iterative")
print(sumBTIterative(None)) # 0
print(sumBTIterative(TreeNode(1, TreeNode(2), TreeNode(3)))) # 6
print(sumBTIterative(TreeNode(1))) # 1
print("Sum of all nodes in BT: recursive")
print(sumBTRecursive(None)) # 0
print(sumBTRecursive(TreeNode(1, TreeNode(2), TreeNode(3)))) # 6
print(sumBTRecursive(TreeNode(1))) # 1


def findMaxBT(root: TreeNode):
    if not root:
        return None
    max_val = root.value
    if root.left:
        max_val = max(max_val, findMaxBT(root.left))
    if root.right:
        max_val = max(max_val, findMaxBT(root.right))
        
    
    return max_val

# Test Cases
print('Find max value recursively')
print(findMaxBT(None)) # None
print(findMaxBT(TreeNode(1, TreeNode(2), TreeNode(3)))) # 3
print(findMaxBT(TreeNode(2, TreeNode(29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9)))))) # 29
print(findMaxBT(TreeNode(1))) # 1


class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def searchBTBFS(root: TreeNode, target: int) -> bool:
    """ BFS """
    if not root:
        return False
    queue = [root]
    while queue:
        cur = queue.pop(0) # pop first - FIFO
        if cur.value == target:
            return True
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return False

# Test Cases
tree1 = TreeNode(3, TreeNode(29, TreeNode(2)), TreeNode(4, None, TreeNode(2, TreeNode(9))))
print(searchBTBFS(None, 1)) # False
print(searchBTBFS(tree1, 9)) # True
print(searchBTBFS(tree1, 1)) # False
print(searchBTBFS(tree1, 2)) # True
print(searchBTBFS(TreeNode(1), 2)) # False

def searchBTDFS(root: TreeNode, target: int) -> bool:
    """ DFS iterative"""
    # if not root:
    #     return False
    # stack = [root]
    # while stack:
    #     cur = stack.pop()
    #     if cur.value == target:
    #         return True
    #     if cur.left:
    #         stack.append(cur.left)
    #     if cur.right:
    #         stack.append(cur.right)
    # return False

    if not root:
        return False
    if root.value == target:
        return True
    return searchBTDFS(root.left, target) or searchBTDFS(root.right, target)


    
        

# Test Cases
tree1 = TreeNode(3, TreeNode(29, TreeNode(2)), TreeNode(4, None, TreeNode(2, TreeNode(9))))
print("DFS recursive:")
print(searchBTDFS(None, 1)) # False
print(searchBTDFS(tree1, 9)) # True
print(searchBTDFS(tree1, 1)) # False
print(searchBTDFS(tree1, 2)) # True
print(searchBTDFS(TreeNode(1), 2)) # False


        
''' Validate BST '''         
def helper(node, min, max):
    if not node:
        return True
    if node.value <= min or node.value >= max:
        return False
    return helper(node.left, min, node.value) and helper(node.right, node.value, max)
        
        
def validateBST(root):
    return helper(root, -float('inf'), float('inf'))



''' 
    2
   1 3
   
   
    1
   2 3
  
     8
   3  10
  1 6   14
       13

'''

tree1 = TreeNode(2,
                TreeNode(1),
                TreeNode(3))
tree2 = TreeNode(1, 
                 TreeNode(2),
                TreeNode(3))
tree3 = TreeNode(8, 
                 TreeNode(3,
                         TreeNode(1),
                         TreeNode(6)),
                TreeNode(10,
                        None,
                        TreeNode(14,
                                TreeNode(13))))
print('Validate BST:')
print(validateBST(None), 'True') # True
print(validateBST(tree1), 'True') # True
print(validateBST(tree2), 'False') # False
print(validateBST(tree3), 'True') # True
print(validateBST(TreeNode()), 'True') # True