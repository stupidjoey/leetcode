class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        count = 0 
        while True:
            digits = self.getDigits(n)
            n = 0
            for d in digits:
                n += d * d
            if n == 1:
                return True
            count += 1
            if count > 20 :
                return False
            
        
        
        
    def getDigits(self, n):
        digits = []
        while n > 0:
            a = n % 10
            n = n /10
            digits.append(a)
        return digits