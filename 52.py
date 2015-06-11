class Solution:
    # @param {integer} n
    # @return {integer}
    def totalNQueens(self, n):
        total_sol = []
        sol = []
        i = 1
        j = 1
        while i > 0:
            while j < n+1:
                if self.checkValidity(i,j,sol):
                    sol.append([i,j])
                    if i == n:
                        total_sol.append(sol[:])
                        sol.pop()
                        break
                    else:
                        i += 1                      
                        j = 1
                else:
                    j += 1       
            i -= 1
            if i <= 0:
                break
            j = sol[-1][1] + 1
            sol.pop()
            
        return len(total_sol)
        
    def checkValidity(self,row,col,sol):
        for pair in sol:
            r = pair[0]
            c = pair[1]
            if row == r or col == c:
                return False
            if abs(row-r) == abs(col-c):
                return False
        return True

        