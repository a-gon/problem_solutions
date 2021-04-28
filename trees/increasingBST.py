from TreeNode import TreeNode

class Solution:
    def __init__(self) -> None:
        self.tree = TreeNode(None)    # points to the beginninng of the new tree

    def increasingBST(self, root: TreeNode) -> TreeNode:
        answer = self.tree
        self.inorder(root)
        return answer.right     # since the first node is a pointer

    def inorder(self, node) -> None:
        """ traverse BST inorder and re-link the nodes """
        if node:
            self.inorder(node.left)
            node.left = None            # cut off the left child 
            self.tree.right = node      # connect previous node with the current
            self.tree = node            # save pointer to current node for further iterations
            self.inorder(node.right)