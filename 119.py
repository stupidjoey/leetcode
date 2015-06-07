class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):

        if rowIndex == 0:
            return [1]
        
        pascal = [1,1]
        for k in range(rowIndex-1):
            temp = [1]
            len_pascal = len(pascal)
            for i in range(0,len_pascal-1):
                temp.append(pascal[i]+pascal[i+1])
            temp.append(1)
            pascal = temp[:]
            
        return pascal