class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        if matrix == []:
            return
        
        m = len( matrix)
        n = len(matrix[0])
        
        row = set(range(m))
        del_row = set()
        del_col = set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    del_row.add(i)
                    del_col.add(j)
        
        for i in del_row:
            matrix[i] = [0] * n
        
        for i in row-del_row:
            for j in del_col:
                matrix[i][j] = 0
        return
     