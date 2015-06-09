class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        
        if m == 0:
            return n
        if n == 0 :
            return m
        
        
        A = [ [ 0 for x in range(n+1)] for y in range(m+1)]
        for i in range(m+1):
            A[i][0] = i
        for j in range(n+1):
            A[0][j] = j
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                a = A[i-1][j] + 1
                b = A[i][j-1] + 1
                if word1[i-1] == word2[j-1]:
                    c = A[i-1][j-1]
                else:
                    c = A[i-1][j-1] + 1
                A[i][j] = min(a,b,c)
                
        return A[m][n]
            