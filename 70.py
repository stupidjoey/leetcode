class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n == 0 or n == 1 or n == 2:
            return n
        A = [0 for x in range(n+1)]
        A[1] = 1
        A[2] = 2
        for i in range(3,n+1):
            A[i] = A[i-1] + A[i-2]  
        return A[n]