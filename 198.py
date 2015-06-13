class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        n = len(nums)
        
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        A = [ 0 for x in range(n+1) ]
        
        A[1] = nums[0]
        
        
        for i in range(2,n+1):
            A[i] = max(A[i-1],A[i-2]+nums[i-1])
            
        return A[n]
        