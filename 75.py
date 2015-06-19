class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    
    # original solution - counting sort
    def sortColors(self, nums):
        
        numdict = {}.fromkeys([0,1,2],0)
        for n in nums:
            numdict[n] += 1
        newnum = []
        for key in [0,1,2]:
            count = numdict[key]
            newnum.extend( [key] * count )            
        for i in range(len(nums)):
            nums[i] = newnum[i]
    
    
    #  new solution : two pointers
    def sortColors(self, nums):
        n  = len(nums)
        i = 0
        j = n
        k = 0
        while k < j and k >= 0:
            if nums[k] < 1:
                temp = nums[i]
                nums[i] = nums[k]
                nums[k] = temp
                i += 1
            elif nums[k] > 1:
                j -= 1
                temp = nums[j]
                nums[j] = nums[k]
                nums[k] = temp
                k -= 1
            k += 1
