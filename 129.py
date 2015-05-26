# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        paths = self.getPath(root)
        sumnum = 0
        for path in paths:
            tempsum = 0
            for val in path:
                tempsum = tempsum * 10 + val
            sumnum += tempsum
        return sumnum
        
    def getPath(self, root):
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [[root.val]]
        left_paths = self.getPath(root.left)
        right_paths = self.getPath(root.right)
        paths = []
        for left in left_paths:
            left.insert(0,root.val)
            paths.append(left)
        for right in right_paths:
            right.insert(0,root.val)
            paths.append(right)
        return paths
            
        

        