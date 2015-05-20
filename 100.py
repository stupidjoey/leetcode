# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        p_inorder = self.inorder_traversal(p)
        p_preorder = self.preorder_traversal(p)
        q_inorder = self.inorder_traversal(q)
        q_preorder = self.preorder_traversal(q)
        print p_inorder,q_inorder
        if p_inorder == q_inorder:
            return True
        else:
            return False
        
    def inorder_traversal(self,root):
        if root == None:
            return None
        else:
            traversal = []
            traversal.append(self.inorder_traversal(root.left))
            traversal.append(root.val)
            traversal.append(self.inorder_traversal(root.right))
            return traversal

            
    def preorder_traversal(self,root):
        if root == None:
            return None
        else:
            traversal = []
            traversal.append(root.val)
            traversal.append(root.left)
            traversal.append(root.right)
            return traversal
        
        
p = TreeNode(1)
s = TreeNode(1)
p.right = s
q = TreeNode(1)
t = TreeNode(1)
q.right = t

sol = Solution()
print sol.isSameTree(p,q)