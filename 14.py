class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        min_len = min(len(x) for x in strs)
        common_prefix = ''
        for i in range(min_len):
            c = strs[0][i]
            for s in strs:
                if s[i] != c:
                    return common_prefix
            common_prefix += c
            
        return common_prefix