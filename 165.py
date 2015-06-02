class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        version1_len = len(version1)
        version2_len = len(version2)
        
        v1 = 0
        endmark1 = 1
        sub_version1 = ""
        if version1_len > 0:
            for idx1 in range(version1_len):
                if version1[idx1] == '.':
                    endmark1 = 0
                    break
            if endmark1 == 1:
                idx1 += 1
            v1 = int(version1[0:idx1])
            sub_version1 = version1[idx1+1:]
        
        v2 = 0 
        endmark2 = 1
        sub_version2 = ""
        if version2_len > 0:
            for idx2 in range(version2_len):
                if version2[idx2] == '.':
                    endmark2 = 0
                    break
            if endmark2 == 1:
                idx2 += 1
            v2 = int(version2[0:idx2])
            sub_version2 = version2[idx2+1:]
        
        if v1 > v2 :
            return 1
        elif v1 < v2 :
            return -1
        else:
            if endmark1 == 1 and endmark2 == 1 :
                return 0 
            else:
                return self.compareVersion(sub_version1,sub_version2)
                
        
        
        