# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        if root == None:
            return
        cur_node = root
        while cur_node != None:
            if cur_node.left != None:
                cur_right = cur_node.right
                cur_left = cur_node.left
                cur_node.right = cur_node.left
                cur_node.left = None
                while cur_left.right !=None:
                    cur_left = cur_left.right
                cur_left.right = cur_right
            cur_node = cur_node.right
        return

        
        
        

node1 = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(1)
node5 = TreeNode(0.5)

node1.left = node2
node2.right = node3
node2.left = node4
node1.right = node5

sol =Solution()
sol.flatten(node1)

c = node1
while c !=None:
    print c.val
    c = c.right


        
