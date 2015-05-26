# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None :
            return 1
        md_left = self.maxDepth(root.left)
        md_right = self.maxDepth(root.right)
        md = 1 + max(md_left,md_right)
        
        return md
        