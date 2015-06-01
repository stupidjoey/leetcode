class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        numberMap = dict()
        numberMap[1000] = 'M'
        numberMap[500] = 'D'
        numberMap[100] = 'C'
        numberMap[50] = 'L'
        numberMap[10] = 'X'
        numberMap[5] = 'V'
        numberMap[1] = 'I'
        
        roman = ''
        if num/1000 > 0 :
            m = num/1000
            roman += numberMap[1000] * m
            num -= m * 1000
        if num/100 > 0 :
            m = num/100
            roman += self.concateRoman(num,numberMap,100,500,1000)
            num -= m * 100
        if num/10 > 0 :
            m = num/10
            roman += self.concateRoman(num,numberMap,10,50,100)
            num -= m * 10
        if num/1 > 0 :
            m = num/1
            roman += self.concateRoman(num,numberMap,1,5,10)
            num -= m * 1                
                        
        return  roman           
    
    def concateRoman(self,num,numberMap,i,i5,i10):
        m = num/i
        if m <= 3:
            roman = numberMap[i] * m
        elif m == 4:
            roman = numberMap[i] + numberMap[i5]
        elif m > 4 and m <=8 :
            roman = numberMap[i5] + numberMap[i] * (m - 5)
        else:
            roman = numberMap[i] + numberMap[i10]
        return roman
          
        
num = 1899
sol = Solution()
print sol.intToRoman(1899)
        