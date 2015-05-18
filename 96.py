class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        count_mat = [[0 for x in range(n+2)] for y in range(n+2) ]
        for i in range(1,n+2):
            count_mat[i][i] = 1
            count_mat[i][i-1] = 1
        for s in range(1,n):
            for i in range(1,n-s+1):
                j = i + s
                temp_count = 0
                for k in range(i,j+1):
                    temp_count += count_mat[i][k-1] * count_mat[k+1][j]
                count_mat[i][j] = temp_count
        return count_mat[1][n]

        




sol = Solution()
print sol.numTrees(2)