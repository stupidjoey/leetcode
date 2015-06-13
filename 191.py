class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        
        b = 1
        count = 0
        while n > 0:
            
            if b & n  == 1:
                count += 1
            
            n = n >> 1
            
        return count