# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def pathSum(self, root, sum):
        if root == None:
            return []
        if root.left == None and root.right == None:
            if root.val == sum:
                return [[sum]]
            else:
                return []
        
        lefts = self.pathSum(root.left, sum - root.val)
        rights = self.pathSum(root.right, sum - root.val)
        
        path = []
        for left in lefts:
            left.insert(0,root.val)
            path.append(left)
        for right in rights:
            right.insert(0,root.val)
            path.append(right)
        return path
        
        