class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        
        nums_len = len(nums)
        if nums_len < 2:
            return nums_len
            
        mark = 1    
        for idx in range(1, nums_len):
            if nums[idx] != nums[idx-1]:
                nums[mark] = nums[idx]
                mark += 1
                
        return mark
    