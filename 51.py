class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
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
        
        transfer_total_sol = self.transfer(total_sol,n)
        return transfer_total_sol
    
    def transfer(self,total_sol, n):
        transfer_total_sol = []
        for sol in total_sol:
            baseform = [ ['.' for x in range(n)] for y in range(n) ]
            for pair in sol:
                i = pair[0]
                j = pair[1]
                baseform[i-1][j-1] = 'Q'
            final_str = ''
            for k in range(n):
                baseform[k] = ''.join(baseform[k])
            transfer_total_sol.append(baseform[:])
             
        return transfer_total_sol
    def checkValidity(self,row,col,sol):
        for pair in sol:
            r = pair[0]
            c = pair[1]
            if row == r or col == c:
                return False
            if abs(row-r) == abs(col-c):
                return False
        return True
        
        
so = Solution()       
print so.solveNQueens(4)    