# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if root == None:
            return True
            
        stack = [root]
        traversal = []
        while set(stack) != set([None]):
            level_stack = []
            level_traversal = []
            for node in stack:
                if node == None:
                    level_traversal.append(None)
                    continue
                level_traversal.append(node.val)
                level_stack.append(node.left)
                level_stack.append(node.right)
            stack = level_stack[:]
            traversal.append(level_traversal)
            
        for tra in traversal:
            for a,b in zip(tra,tra[::-1]):
                if a != b:
                    return False
        return True
            
                