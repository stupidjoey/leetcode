class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        len_a = len(a)
        len_b = len(b)
        max_len = max(len_a,len_b)
        finalstr = ["0"] * max_len
        a = "0" * (max_len - len_a) + a
        b=  "0" * (max_len - len_b) + b

        extra = 0
        for i in range(max_len-1,-1,-1):
            ai = int(a[i])
            bi = int(b[i])
            sumall = ai+bi+extra
            finalstr[i] = str(sumall % 2)
            if sumall >= 2:
                extra = 1
            else:
                extra = 0
        if extra == 1:
            finalstr.insert(0,"1")
        finalstr = ''.join(finalstr)
        return finalstr


a = "101"
b = "1"
sol = Solution()
print sol.addBinary(a,b)