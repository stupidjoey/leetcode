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
                