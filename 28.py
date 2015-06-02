class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        needle_len = len(needle)
        if needle_len == 0:
            return 0
        
        for idx in range(0, len(haystack)-needle_len + 1):
            substr = haystack[idx:idx+needle_len]
            if substr == needle:
                return idx
                
        return -1
            
        