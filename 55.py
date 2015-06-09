class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        
        nums_len = len(nums)
        if nums_len == 0:
            return True
        cur_idx = 0
        while cur_idx < nums_len-1 :
            jump_len = nums[cur_idx]
            if jump_len == 0:
                return False
            if cur_idx + jump_len >= nums_len-1:
                return True
            
            max_jump = 0
            for idx in range(cur_idx+1 ,cur_idx + jump_len + 1):
                if idx + nums[idx] >= max_jump:
                    max_jump = idx + nums[idx]
                    cur_idx = idx
                    
        return True