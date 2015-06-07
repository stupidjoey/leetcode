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