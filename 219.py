class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        nums_len = len(nums)
        num_dict = dict()
        for idx in range(nums_len):
            n = nums[idx]
            num_dict.setdefault(n,[])
            num_dict[n].append(idx)
        for key in num_dict.keys():
            idxs = num_dict[key]
            idxs_len = len(idxs)
            if idxs_len >= 2:
                for i in range(0,idxs_len-1):
                    for j in range(i+1,idxs_len):
                        temp_diff = abs(idxs[i]-idxs[j])
                        if temp_diff <= k:
                            return True
        return False
                