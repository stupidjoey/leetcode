class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        slen = len(s)
        if slen == 0:
            return 0
        count = 0
        mark = 0
        for c in s[::-1]:
            if c == ' ':
                if mark == 0:
                    continue
                else:
                    break
            else:
                count += 1
                mark = 1
        return count