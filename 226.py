# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root == None:
            return None
        
        
        
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        
        temp = root.left
        root.left = root.right
        root.right = temp
        
        return root
        