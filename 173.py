# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
       self.stack = self.left_traversal(root)

    def left_traversal(self, root):
        if root == None:
            return []
        tra = [root]
        while root.left != None:
            tra.append(root.left)
            root = root.left
        return tra

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if len(self.stack) >= 1:
            return True
        else:
            return False

    # @return an integer, the next smallest number
    def next(self):
        minNode = self.stack.pop()
        if minNode.right != None:
            self.stack.extend( self.left_traversal(minNode.right))
        return minNode.val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())


root = TreeNode(5)
n1 = TreeNode(2)
n2 = TreeNode(7)
root.left = n1
root.right = n2
n3 = TreeNode(6)
n4 = TreeNode(8)
n2.left = n3
n3.right= n4

i, v = BSTIterator(root), []
while i.hasNext(): v.append(i.next())

print v