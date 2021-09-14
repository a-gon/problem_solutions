class Node:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

def printTree(root, result):
    if not root:
        return result.append(None)
    result.append(root.val)
    if not root.left and not root.right:
        return 
    printTree(root.left, result)
    printTree(root.right, result)



def findNextVal(root):
#         applying inorder traversal - root is parent, what would be the next val
#         next val is the smallest val in the right subtree

        root = root.right
        while root.left:
            root = root.left
        return root.val
    
def findPrevVal(root):
#         applying inorder traversal - root is parent, what was previous val
#         prev val is the greatest val if the left subtree

    root = root.left
    while root.right:
        root = root.right
    return root.val

def deleteNode(root, key: int):
    if not root:
        return None
    if key < root.val:
        root.left = deleteNode(root.left, key)
    if key > root.val:
        root.right = deleteNode(root.right, key)
    if key == root.val:
        if not root.right and not root.left:   # leaf node - just delete
            root = None
        elif root.right:
            root.val = findNextVal(root)   # replace node val with next val
            root.right = deleteNode(root.right, root.val)    # delete the next val node in right subtree
        elif root.left:
            root.val = findPrevVal(root)   # replace node val with prev val
            root.left = deleteNode(root.left, root.val)   # delete the prev val node in left subtree
    return root


'''
        5
    3       6
  2   4       7



'''

tree1 = Node(5, 
    Node(3, 
        Node(2),
        Node(4)),
    Node(6,
        None,
        Node(7)))

newTree = deleteNode(tree1, 3)
result = []
printTree(newTree, result)
print(result)