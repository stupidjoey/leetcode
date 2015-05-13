# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        if root == None :
            return []
        else:
            output = []
            queue = [root]
            while len(queue) > 0:
                level_output = []
                temp_queue = []
                for node in queue:
                    level_output.append(node.val)
                    leftnode = node.left
                    rightnode = node.right
                    if leftnode != None:
                        temp_queue.append(leftnode)
                    if rightnode != None:
                        temp_queue.append(rightnode)
                queue = temp_queue[:]
                output.append(level_output)
                        
            return output