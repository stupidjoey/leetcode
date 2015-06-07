class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        if n == 0:
            return []
        matrix = [ [0 for x in range(n)] for y in range(n)]
        if n % 2 == 0:
            row = n/2 - 1
        else:
            row = n/2
        count = 1
        n_square = n * n
        for i in range(0, row + 1):
            
            for j in range(i,n-i):
                if count > n_square:
                    break
                matrix[i][j] = count
                count += 1

            
            for k in range(i+1,n-i-1):
                if count > n_square:
                    break
                matrix[k][n-i-1] = count
                count += 1
              
            
            for j in range(n-i-1,i-1,-1):
                if count > n_square:
                    break
                matrix[n-i-1][j] = count
                count += 1
              
            for k in range(n-i-2,i,-1):
                if count > n_square:
                    break
                matrix[k][i] = count
                count += 1
             
        return matrix
        
        
        