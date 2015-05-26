# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if root == None:
            return False
            
        if root.left == None and root.right == None:
            if root.val == sum:
                return True
            else:
                return False
        
        left_flag = self.hasPathSum(root.left, sum - root.val)
        right_flag = self.hasPathSum(root.right, sum - root.val)
        
        
        if left_flag or right_flag:
            return True
        else:
            return False
        