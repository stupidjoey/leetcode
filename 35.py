class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        nums_len = len(nums)
        if nums_len == 0 :
            return 0
        
        p_idx = nums_len/2
        p = nums[p_idx]
        if target > p:
            find_idx =  self.searchInsert(nums[p_idx+1:], target)
            return find_idx + p_idx + 1
        elif target == p:
            return p_idx
        else:
            find_idx = self.searchInsert(nums[0:p_idx], target)
            return find_idx

            
        