class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        num_map = dict()
        for i in range(1,27):
            num_map[i] = chr(i+64)
        final_str = []
        while n >26:
            m = (n-1) / 26
            a = n - 26 * m
            n = m 
            final_str.insert(0, num_map[a])
        final_str.insert(0, num_map[n])
        final_str = ''.join(final_str)
        return final_str
            
            
        