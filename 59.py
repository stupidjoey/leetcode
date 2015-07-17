class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix1(self, n):
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
    
    # new solution 
    def generateMatrix(self, n):
        mat = [ [0 for x in range(n)] for y in range(n)]
        i = 0
        k = 1
        while k <= n * n:
            j = i
            #  to right
            while j < n - i:
                mat[i][j] = k
                j += 1
                k += 1
            j = i + 1
            # down
            while j < n - i-1 :
                mat[j][n-i-1] = k
                j += 1
                k += 1
            
            j = n - i - 1
            ## to left
            while j >i:
                mat[n-i-1][j] = k
                j -= 1
                k += 1
            
            j = n - i - 1
            # up
            while j >i :
                mat[j][i] = k
                j -= 1
                k += 1
            
            i += 1
            
        return mat
            
               
sol = Solution()
print sol.generateMatrix(2)