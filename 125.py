class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        s = str(s)
        s = s.strip()
        s = s.lower()
        s = filter(str.isalnum, s)
        slen = len(s)
        if slen == 0:
            return True
        else:           
            for i,j in zip(range(0,slen),range(slen-1,-1,-1)):
                if i > j:
                    break
                a = s[i]
                b = s[j]
                if a != b:
                    return False
            return True
        
    # new solution     
    def isPalindrome(self, s):
        n = len(s)
        i = 0
        j = n-1
        while i < j:
            while i < j and  (not s[i].isalnum()):
                i += 1
            while i < j and ( not s[j].isalnum()):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True

        
s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
sol = Solution()
s3 = "1a2"
print str(s3)
print sol.isPalindrome(s2)
