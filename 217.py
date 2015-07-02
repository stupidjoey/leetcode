class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        numsdict = dict()
        for n in nums:
            numsdict.setdefault(n,0)
            numsdict[n] += 1
        
        for key in numsdict.keys():
            if numsdict[key] > 1:
                return True
        return False


    # new solution 
    def containsDuplicate(self, nums):
        
        nums_map = dict()
        for n in nums:
            if n in nums_map:
                return True
            nums_map[n] = 1
        return False