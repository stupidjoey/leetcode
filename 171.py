class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        char_map = dict()
        for i in range(1,27):
            char_map[chr(i+64)] = i
        s_len = len(s)
        num = 0
        level = 0
        for i in range(s_len-1,-1,-1):
            cur_char = s[i]
            num += char_map[cur_char] * (26**level)
            level += 1
        return num
            