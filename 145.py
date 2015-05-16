# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        if root == None:
            return []
        stack = [root]
        traversal = []
        visit = []
        while len(stack) != 0:
            root = stack[0]
            if root.left != None:
                if root.left not in visit:
                    stack.insert(0,root.left)
                    continue
            if root.right != None:
                if root.right not in visit:
                    stack.insert(0,root.right)
                    continue
            visit.append(stack.pop(0))
            traversal.append(root.val)
        return traversal