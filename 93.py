class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        slen = len(s)
        if slen == 0:
            return []
        total_ipset = self.cutstr(s, 4)
        return total_ipset
        
    def cutstr(self, s, count):
        if count == 1:
            if len(str(int(s))) != len(s)  or int(s) > 255:
                return []
            else:
                return [s]
        total_ipset = []
        for k in range(1,4):
            if len(s) < k:
                continue
            cur_str = s[0:k]
            if len(str(int(cur_str))) != len(cur_str):
                continue
            if int(cur_str) > 255 :
                continue
            left_s = s[k:]
            if len(left_s) < (count - 1) or len(left_s) > 3 * (count -1):
                continue
            cur_ipset = []
            sub_ipset = self.cutstr(left_s, count-1)
            if len(sub_ipset) == 0:
                continue
            for ip in sub_ipset:
                cur_ipset.append(cur_str + '.' + ip)
            total_ipset.extend(cur_ipset)  
        return total_ipset
                
            
        