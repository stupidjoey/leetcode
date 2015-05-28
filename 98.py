# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isValidBST(self, root):
        traversal,flag = self.checkBST(root)
        return flag
        
    def checkBST(self, root):
        if root == None:
            return [],True
        if root.left == None and root.right == None:
            return [root.val],True
        left_traversal,left_flag = self.checkBST(root.left)
        right_traversal,right_flag = self.checkBST(root.right)

        if left_flag == True and right_flag == True:
            traversal = left_traversal[:]
            traversal.append(root.val)
            traversal.extend(right_traversal)

            if len(left_traversal) > 0:
                if left_traversal[-1] < root.val:
                    left_mark = True
                else:
                    left_mark = False
            else:
                left_mark = True

            if len(right_traversal) > 0:
                if right_traversal[0] > root.val:
                    right_mark = True
                else:
                    right_mark = False
            else:
                right_mark = True
            if left_mark == True and right_mark == True:
                return traversal,True
            else:
                return None,False

        else:
            return None,False
            
            
root = TreeNode(0)
leftnode = TreeNode(-1)
root.left = leftnode
sol =Solution()
print sol.isValidBST(root)