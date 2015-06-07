class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        nums_len = len(nums)
        if nums_len == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[nums_len-1] > nums[nums_len-2]:
            return nums_len-1
        
        for i in range(1,nums_len-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        
        
        