# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def recoverTree(self, root):
        if root == None:
            return
        traversal = self.recoverBST(root)
        return
        
    def recoverBST(self, root):
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root]
        left_traversal = self.recoverBST(root.left)
        right_traversal = self.recoverBST(root.right)

        if left_traversal != None and right_traversal != None:
            traversal = left_traversal[:]
            traversal.append(root)
            traversal.extend(right_traversal)
            
            if len(left_traversal) > 0:
                if left_traversal[-1].val > root.val:
                    print 
                    self.swapval(left_traversal[-1],root)
                    return None
            if len(right_traversal) > 0:
                if right_traversal[0].val < root.val:
                    self.swapval(right_traversal[0],root)
                    return None
                    
            if len(left_traversal) > 0 and  len(right_traversal) > 0:
                if left_traversal[-1].val >  right_traversal[0].val:
                    self.swapval(left_traversal[-1], right_traversal[0])
                    return None
   
            return traversal
        else:
            return None
            
    def swapval(self,node1,node2):
        temp = node1.val
        node1.val = node2.val
        node2.val = temp
        
        

node1 = TreeNode(0)
node2 = TreeNode(1)

node1.left = node2
sol = Solution()

sol.recoverTree(node1)

print node1.val