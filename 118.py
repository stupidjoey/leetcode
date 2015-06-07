class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        
        if numRows == 0:
            return []
        
        if numRows == 1:
            return [[1]]
        
        pascal = [[]] * numRows
        pascal[0] = [1]
        pascal[1] = [1,1]
        for k in range(2,numRows):
            temp = [1]
            pre_pascal = pascal[k-1]
            len_pre = len(pre_pascal)
            for i in range(0,len_pre-1):
                temp.append(pre_pascal[i]+pre_pascal[i+1])
            temp.append(1)
            pascal[k] = temp[:]
            
        return pascal
                    
            
        