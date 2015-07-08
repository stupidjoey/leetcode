class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        
        max_sum = -float('inf')
        current_sum = 0
        for n in nums:
            current_sum += n
            max_sum = max(max_sum, current_sum)
            if current_sum < 0:
                current_sum = 0

               
        return max_sum

    # dynamic programming
    def maxSubArray(self, nums):
        n = len(nums)
        max_sum = nums[0]
        A = [0] * n
        A[0] = nums[0]
        for i in range(1,n):
            if A[i-1] < 0:
                A[i] = nums[i]
            else:
                A[i] = A[i-1] + nums[i]
            max_sum = max(A[i], max_sum)
        
        return max_sum


    # divide and conquer
    def maxSubArray(self, nums):
        n = len(nums)
        return self.divide_conquer(nums, 0, n-1)
        
    def divide_conquer(self,nums,left,right):
        if left == right:
            return nums[left]
        
        mid = (right + left)/2 
        max_left = self.divide_conquer(nums,left,mid)
        max_right = self.divide_conquer(nums,mid+1,right)
        
        m_left = nums[mid]
        temp_left = 0
        for i in range(mid,left-1,-1):
            temp_left += nums[i]
            m_left = max(m_left,temp_left)
        m_right = nums[mid+1]
        temp_right = 0
        for i in range(mid+1,right+1):
            temp_right += nums[i]
            m_right = max(m_right,temp_right)
            
        return max( max(max_left,max_right), m_left + m_right  )
            