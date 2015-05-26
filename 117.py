# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return
        stack = [root]
        while len(stack) > 0:
            len_stack = len(stack)
            level_stack = []
            for idx in range(0,len_stack):
                node = stack[idx]
                if node.left != None:
                    level_stack.append(node.left)
                if node.right != None:
                    level_stack.append(node.right)
                if idx != len_stack -1:
                    node.next = stack[idx+1]
            stack = level_stack[:]
        return 