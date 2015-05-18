# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def generateTrees(self, n):
        treemat = [ [[] for x in range(n+2)] for y in range(n+2) ]
        for i in range(1,n+2):
            treemat[i][i] = [TreeNode(i)]
            treemat[i][i-1] = [None]
            
        print treemat
        for s in range(1,n):
            for i in range(1,n-s+1):
                j = i + s
                for k in range(i, j+1):
                    temproot = TreeNode(k)  
                    left_tree = treemat[i][k-1]
                    right_tree = treemat[k+1][j]

                    for left in left_tree:
                        for right in right_tree:
                            temproot.left = left
                            temproot.right = right 
                            treemat[i][j].append(temproot)
                            # print self.preorderTraversal(temproot)
        for root in treemat[1][n][:]:
            print self.preorderTraversal(root)
        return  treemat[1][n][:]
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

sol = Solution()
roots = sol.generateTrees(3)
print len(roots)
for root in roots:
    print sol.preorderTraversal(root)