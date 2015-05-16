# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        root = TreeNode(postorder.pop())
  
        rootidx = inorder.index(root.val)
        leftinorder = inorder[0:rootidx]
        rightinorder = inorder[rootidx+1:]
        
        root.right = self.buildTree(rightinorder,postorder)
        root.left = self.buildTree(leftinorder,postorder)
       
        
        return root
    def preorderTraversal(self, root):
        if root == None:
            return []
        stack = [root]
        traversal = []
        while len(stack)!= 0:
            root = stack.pop(0)
            traversal.append(root.val)
            if root.right != None:
                stack.insert(0,root.right)
            if root.left != None:
                stack.insert(0,root.left)
        return traversal
    
    def postorderTraversal(self, root):
        if root == None:
            return []
        stack = [root]
        traversal = []
        while len(stack) != 0:
            vallist = [x.val for x in stack]
            root = stack[0]
            if root.left != None:
                if root.left.val not in traversal:
                    stack.insert(0,root.left)
                    continue
            if root.right != None:
                if root.right.val not in traversal:
                    stack.insert(0,root.right)
                    continue
            stack.pop(0)
            traversal.append(root.val)
        return traversal
    
    def inorderTraversal(self, root):
        if root == None:
            return []
        stack = [root]
        traversal = []
        visit = []
        while len(stack)>0:
            root = stack[0]
            if root.left != None:
                if root.left not in visit:
                    stack.insert(0,root.left)
                    continue
            stack.pop(0)
            traversal.append(root.val)
            visit.append(root)
            if root.right != None:
                stack.insert(0,root.right)
        return traversal
    
    
    
    def inorder_traversal(self,root):
        if root == None:
            return []
        else:
            traversal = []
            traversal.extend(self.inorder_traversal(root.left))
            traversal.append(root.val)
            traversal.extend(self.inorder_traversal(root.right))          
            return traversal    
     

     
        
sol = Solution()
# inorder = [1,2,3,4,5,6,7,8]
# postorder = [1,3,4,2,7,6,8,5]
inorder = [-4,-10,3,-1,7,11,-8,2]
postorder = [-4,-1,3,-10,11,-8,2,7]
root = sol.buildTree(inorder,postorder)
# print sol.preorderTraversal(root)
print sol.inorderTraversal(root)


