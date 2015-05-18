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
        Roots = []
        treemat = [ [None for x in range(n+2)] for y in range(n+2) ]
        for i in range(1,n+1):
            treemat[i][i] = TreeNode(i)

        for s in range(1,n):
            for i in range(1,n-s+1):
                j = i + s
                for k in range(i, j+1):
                    temproot = TreeNode(k)  
                    temproot.left = treemat[i][k-1]
                    temproot.right = treemat[k+1][j]
                    Roots.append(temproot)
        
        return  Roots


sol = Solution()
roots = sol.generateTrees(2)
print len(roots)
for root in roots:
    print root.val