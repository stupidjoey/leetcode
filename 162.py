class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement0(self, nums):
        nums_len = len(nums)
        if nums_len == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[nums_len-1] > nums[nums_len-2]:
            return nums_len-1
        
        for i in range(1,nums_len-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        
    # new solution O(n)
    def findPeakElement(self, nums):
        n = len(nums)

        for i in range(1,n):
            if nums[i] < nums[i-1]:
                return i-1
        
        return n-1


    # new solution binary search
    def findPeakElement(self, nums):
        n = len(nums)
        low = 0
        high = n - 1
        
        while low < high:
            mid = (low + high)/2
            if nums[mid] < nums[mid+1]:
                low = mid + 1
            else:
                high = mid
        
        return low

        
sol = Solution()
nums = [1,2,3,1]
print sol.findPeakElement(nums)