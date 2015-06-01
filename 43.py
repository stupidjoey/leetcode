class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        num1_list = map(int, num1)
        num1_list = num1_list[::-1]
        num2_list = map(int, num2)
        num2_list = num2_list[::-1]
        
        len_num1 = len(num1)
        len_num2 = len(num2)
        result = [0] * (len_num1 + len_num2 + 1)
        
        for i in range(len_num1):
            n1 = num1_list[i]
            for j in range(len_num2):
                n2 = num2_list[j]
                result[i+j] += n1 * n2
        
        extra = 0 
        for k in range(len(result)):
            result[k] += extra
            extra = result[k]/10
            result[k] %= 10
        
        for r in result[::-1]:
            if r > 0:
                break
            else:
                result.pop()
        
        finalStr = ''
        for r in result[::-1]:
            finalStr += str(r)
            
        return finalStr
            
        
        