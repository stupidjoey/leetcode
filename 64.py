class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        temp = grid[0][0]
        for i in range(1,m):
            grid[i][0] += temp
            temp = grid[i][0]
            
        temp = grid[0][0]
        for j in range(1,n):
            grid[0][j] += temp
            temp = grid[0][j]
        
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                
        return grid[m-1][n-1]
        
        
        
        