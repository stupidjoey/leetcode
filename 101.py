# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if root == None:
            return True
        left_traversal = self.inorder_traversal(root.left)
        right_traversal = self.inorder_traversal(root.right)
        print left_traversal
        print right_traversal
        len_left = len(left_traversal)
        len_right = len(right_traversal)
        if len_left != len_right:
            return False
        for i,j in zip(range(0,len_left), range(len_right-1,-1,-1)):
            if left_traversal[i] != right_traversal[j]:
                return False
        return True
                
        
        
        
    def inorder_traversal(self, root):
        if root == None:
            return [null]
        traversal = []
        traversal.extend( self.inorder_traversal(root.left))
        traversal.append(root.val)
        traversal.extend( self.inorder_traversal(root.right))
        return traversal



sol = Solution()
r1 = TreeNode(1)
r2 = TreeNode(2)
r3 = TreeNode(3)
r4 = TreeNode(3)
r5 = TreeNode(2)

r2.left = r4
r3.left = r5
r1.left = r2
r1.right = r3

print sol.isSymmetric(r1)
print sol.inorder_traversal(r1)