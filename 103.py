# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def zigzagLevelOrder(self, root):
        if root == None:
            return []
        stack = [root]
        traversal = []
        count = 0
        while len(stack) > 0:
            level_stack = []
            level_traversal = []
            for node in stack:
                level_traversal.append(node.val)
                if node.left != None:
                    level_stack.append(node.left)
                if node.right != None:
                    level_stack.append(node.right)
            stack = level_stack[:]       
            if count % 2 == 1:
                level_traversal = level_traversal[::-1]
            traversal.append(level_traversal)        
            count += 1
                
        return traversal
            