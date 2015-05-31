class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        
        cur_s = '1'
        while n > 1:
            cur_s = self.generateSequence(cur_s)
            n = n - 1
        return cur_s
        
    def generateSequence(self, n_str):
        count = 0
        pre_s = n_str[0]
        finals = ""
        for s in n_str:
            if s == pre_s:
                count += 1
            else:
                finals += str(count) + pre_s
                pre_s = s
                count = 1
        finals += str(count) + pre_s
        return finals