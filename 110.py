# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        root_depth,flag = self.checkBalance(root)
        return flag
        
    def checkBalance(self, root):
        if root == None:
            return 0,True
        left_depth,left_flag = self.checkBalance(root.left)
        right_depth,right_flag = self.checkBalance(root.right)
        current_depth = max(left_depth, right_depth) + 1
        if left_flag == True and right_flag == True:
            if abs(left_depth - right_depth) <= 1:
                return current_depth, True
        return current_depth,False
        