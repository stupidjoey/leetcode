class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        n = len(nums)
        if n == 0:
            return [-1,-1]
        if n == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
        mid = n/2
        mid_val = nums[mid]
        if target < mid_val:
            the_range = self.searchRange(nums[0:mid], target)
            return the_range
        elif target > mid_val:
            the_range = self.searchRange(nums[mid+1:], target)
            if the_range[0] == -1:
                return the_range
            else:
                return [the_range[0]+mid+1, the_range[1]+mid+1]
        else:
            start_idx = mid - 1
            while start_idx >= 0:
                if nums[start_idx] == target:
                    start_idx -= 1
                else:
                    break
            start_idx += 1
            
            end_idx = mid + 1
            while end_idx <= n-1 :
                if nums[end_idx] == target:
                    end_idx += 1
                else:
                    break
            end_idx -= 1   
            
            return [start_idx,end_idx]
        
        