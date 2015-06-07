class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        nums_len = len(nums)
        if nums_len == 0:
            return float('inf')
        
        if nums_len == 1:
            return nums[0]
        
        
        p_idx = nums_len/2
        p = nums[p_idx]
        left_min = self.findMin(nums[0:p_idx])
        right_min = self.findMin(nums[p_idx+1:])
        
        
        
        return min(p, left_min, right_min)