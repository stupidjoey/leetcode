# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxPathSum(self, root):
        if root == None:
            return None
        else
            
        
    def getMax(self, root):
        if root == None:
            return -float("inf"),-float("inf")
        if root.left == None and root.right == None:
            return root.val
        left_max,left_cur_max = self.getMax(root.left)
        right_max,right_cur_max = self.getMax(root.left)
        lr_max = max(left_max,right_max)
        current_max = max(lr_max, root,val,left_cur_max,right_cur_max )
        if lr_max <= 0:
            the_max = root.val
        else:
            the_max = lr_max + root.val
        return the_max,current_max
        