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
            newnum.extend( [key] * count)
            
        for i in range(len(nums)):
            nums[i] = newnum[i]
        