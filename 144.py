# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        if root == None:
            return []
        stack = [root]
        traversal = []
        while len(stack)!= 0:
            root = stack.pop(0)
            traversal.append(root.val)
            if root.right != None:
                stack.insert(0,root.right)
            if root.left != None:
                stack.insert(0,root.left)
        return traversal