class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        
        nums1_copy = nums1[0:m][:]
        i = 0
        j = 0
        for mark in range(m+n):
            if i >= m:
                nums1[mark:(m+n)] = nums2[j:]
                break
            if j >= n:
                nums1[mark:(m+n)] = nums1_copy[i:]
                break
            
            
            if nums1_copy[i] <= nums2[j]:
                nums1[mark] = nums1_copy[i]
                i += 1
            else:
                nums1[mark] = nums2[j]
                j += 1
            
        return