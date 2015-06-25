class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        stack = []
        max_sublen = 0
        for c in s:
            if c not in stack:
                stack.append(c)
                max_sublen = max(max_sublen, len(stack))
            else:
                idx = stack.index(c)
                stack = stack[idx+1:]
                stack.append(c)
        return max_sublen
    
    # new solution 
    def lengthOfLongestSubstring(self, s):
        i = 0
        smap = {}
        max_len = 0
        n = len(s)
        for k in range(n):
            c = s[k]
            if c in smap:
                i = max(smap[c]+1, i)
            smap[c] = k
            max_len = max(max_len, k-i+1)
        return max_len