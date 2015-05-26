# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
            
        md_left = self.minDepth(root.left)
        md_right = self.minDepth(root.right)
        
        md = 0
        if md_left != 0 and md_right != 0:
            md = min(md_left,md_right) + 1
        if md_left == 0:
            md = md_right +1
        if md_right == 0:
            md = md_left + 1

        
        return md
        