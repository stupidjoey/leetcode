class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        nums.sort()
        nums_len = len(nums)
        subset = [nums]
        if nums != []:
            subset.append([])
        temp =  [nums]
        count = nums_len
        while count > 0:
            ttemp = []
            for temp_num in temp:
                temp_num_len = len(temp_num)
                for i in range(temp_num_len):
                    a = temp_num[:]
                    a[i:i+1] = []
                    if a not in subset:
                        subset.append(a)
                        ttemp.append(a)
            temp = ttemp[:]
            count -= 1
        return subset