class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        A = [[ 0 for x in range(n+1)] for y in range(m+1)]
        for i in range(1,m+1):
            A[i][1] = 1
        for j in range(1,n+1):
            A[1][j] = 1
        
        for i in range(2,m+1):
            for j in range(2, n+1):
                A[i][j] = A[i-1][j] + A[i][j-1]
        
        return A[m][n]
        
        
        