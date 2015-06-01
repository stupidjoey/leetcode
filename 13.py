class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        s_len = len(s)
        if s_len == 0:
            return 0
        romanMap = dict()
        romanMap['I'] = 1
        romanMap['V'] = 5
        romanMap['X'] = 10
        romanMap['L'] = 50
        romanMap['C'] = 100
        romanMap['D'] = 500
        romanMap['M'] = 1000
        romanMap['W'] = 0  # special case
        
        interger = 0
        last_r = s[-1]
        temp = romanMap[last_r]
        
        for idx in range(s_len-2,-1,-1):
            r = s[idx]
            if r == last_r:
                temp += romanMap[r]
            else:
                if romanMap[r] > romanMap[last_r]:
                    interger += temp
                    last_r = r
                    temp = romanMap[r]
                elif romanMap[r] < romanMap[last_r]:
                    interger += temp - romanMap[r]
                    last_r = 'W'
                    temp = 0
                    
        interger += temp
        return interger
                    
            
            
        
            