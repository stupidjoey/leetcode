class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        nums_len = len(nums)
        numdict = dict()
        
        for n in nums:
            numdict.setdefault(n,0)
            numdict[n] += 1
        
        max_time = nums_len/2
        max_num = 0
        for key in numdict.keys():
            if numdict[key] > max_time:
                max_time =  numdict[key]
                max_num = key
                
        return max_num

    # new solution 
    def majorityElement(self, nums):
        
        maj = nums[0]
        pointer = 1
        
        for n in nums[1:]:
            if pointer == 0:
                maj = n
                pointer = 1
            else:
                if n == maj:
                    pointer += 1
                else:
                    pointer -= 1
        return maj
    