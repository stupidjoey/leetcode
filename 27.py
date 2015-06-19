class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    
    # original solution
    def removeElement(self, nums, val):
        nums[:] = [x for x in nums if x != val]
        return len(nums)
        
    
    # new solution
    def removeElement(self, nums, val):
        n = len(nums)
        j = 0
        for i in range(n):
            cur_num = nums[i]
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1

        return j