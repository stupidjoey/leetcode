# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        if len(preorder)==0 or len(inorder) == 0:
            return None
        root = TreeNode(preorder.pop(0))
        rootidx = inorder.index(root.val)
        leftinorder = inorder[0:rootidx]
        rightinorder = inorder[rootidx+1:]
        root.left = self.buildTree(preorder,leftinorder)
        root.right = self.buildTree(preorder,rightinorder)
        
        return root