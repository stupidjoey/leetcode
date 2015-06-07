class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        
        if matrix == []:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        cur_row = -1
        for row in range(m):
            if matrix[row][n-1] >= target:
                cur_row = row
                break
        if cur_row == -1:
            return False
        
        cur_list = matrix[cur_row]
        while len(cur_list) > 0:
            p_idx = len(cur_list)/2
            p = cur_list[p_idx]
            if target > p:
                cur_list = cur_list[p_idx+1:]
            elif target == p:
                return True
            else:
                cur_list = cur_list[:p_idx]
        return False
        
        
        
        
        