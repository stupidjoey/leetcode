class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        if matrix == []:
            return matrix
        m = len(matrix)
        if m == 1:
            return matrix[0]
        if matrix[0] == []:
            return []
            
        n = len(matrix[0])
        if n == 1:
            return [matrix[i][0] for i in range(m)]
        
        spiral_order = []
        
        spiral_order.extend(matrix[0])
        for k in range(1, m-1):
            spiral_order.append(matrix[k][n-1])
            matrix[k][n-1:] = []
        
        spiral_order.extend(matrix[m-1][::-1])
        
        for k in range(m-2,0,-1):
            spiral_order.append(matrix[k][0])
            matrix[k][0:1] = []
        
        sub_order = self.spiralOrder(matrix[1:m-1])
        spiral_order.extend(sub_order)
        
        return spiral_order
        
        
        