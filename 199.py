# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        if root == None:
            return []
        stack = [root]
        traversal = []
        while len(stack) > 0 :
            level_stack = []
            level_traversal = []
            for node in stack:
                level_traversal.append(node.val)
                if node.left != None:
                    level_stack.append(node.left)
                if node.right !=None:
                    level_stack.append(node.right)
            stack = level_stack[:]
            traversal.append(level_traversal)
        rightview = []
        for level_traversal in traversal:
            rightview.append(level_traversal[-1])
        return rightview
            
        