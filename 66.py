class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        extra = 1
        digits_len = len(digits)
        for idx in range(digits_len-1,-1,-1):
            temp_sum = digits[idx] + extra
            if temp_sum >= 10:
                extra = 1
            else:
                extra = 0
            
            digits[idx] = temp_sum % 10
        
        if extra == 1:
            digits.insert(0,1)
        
        return digits