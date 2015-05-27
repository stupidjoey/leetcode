class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        final_s = []
        len_s = len(s)
        for row in range(numRows):
            cur_idx = row
            temp_s = []
            while cur_idx <= (len_s-1):
                temp_s.append(s[cur_idx])
                cur_idx += 2 * (numRows - 1)
            if row in range(1,numRows-1):
                cur_idx2 = (numRows - row - 1) * 2 + row
                temp_s2 = []
                while cur_idx2 <= (len_s-1):
                    temp_s2.append(s[cur_idx2])
                    cur_idx2 += 2 * (numRows - 1)
                if len(temp_s) > len(temp_s2):
                    for a,b in zip(temp_s[:-1],temp_s2):
                        final_s.append(a)
                        final_s.append(b)
                    final_s.append(temp_s[-1])
                else:
                     for a,b in zip(temp_s,temp_s2):
                        final_s.append(a)
                        final_s.append(b)
            else:
                final_s.extend(temp_s)
                
        return ''.join(final_s)
                
sol = Solution()
s="ABDS"
print sol.convert(s,3)