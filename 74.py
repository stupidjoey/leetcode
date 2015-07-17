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
        
        
    # new solution
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        
        low = 0
        high = m - 1
        
        while low < high:
            mid = (low + high)/2
            if matrix[mid][n-1] >= target:
                high = mid
            else:
                low = mid + 1
        row = low
        left = 0 
        right = n - 1
        
        while left <= right:
            mid = (left + right)/2
            if matrix[row][mid] == target :
                return True
            elif  matrix[row][mid] > target :
                right = mid - 1
            elif matrix[row][mid] < target:
                left = mid + 1
        return False
    
    # new solution 
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        
        low = 0
        high = m * n -1
        
        while low <= high:
            mid = (low + high)/2
            val = matrix[mid/n][mid%n]
            
            if val > target:
                high = mid - 1
            elif val == target:
                return True
            else:
                low = mid + 1
            
        
        return False   
        