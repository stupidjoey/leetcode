class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        nums_len = len(nums)
        if nums_len == 0 :
            return [[]]
        if nums_len == 1:
            return [nums]
        
        total_permu = []
        nums_set = set(nums)
        for num in nums_set:
            sub_permu = self.permute(list(nums_set - set([num]))  )
            for p in sub_permu:
                p.insert(0,num)
                total_permu.append(p)
        
        return total_permu