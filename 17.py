class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        dlen = len(digits)
        if dlen == 0 :
            return []
        digit_map = dict()
        digit_map['2'] = ['a','b','c']
        digit_map['3'] = ['d','e','f']
        digit_map['4'] = ['g','h','i']
        digit_map['5'] = ['j','k','l']
        digit_map['6'] = ['m','n','o']
        digit_map['7'] = ['p','q','r','s']
        digit_map['8'] = ['t','u','v']
        digit_map['9'] = ['w','x','y','z']
        digit_map['0'] = [' ']
        
        d0 = digits[0]
        output = digit_map[d0]
        for d in digits[1:]:
            strset = digit_map[d]
            temp_output = output[:]
            output = []
            for c in strset:
                for out in temp_output:
                    out += c
                    output.append(out)

                    
        return output
        
        
        
        
sol = Solution()
digits = '22'
print sol.letterCombinations(digits)