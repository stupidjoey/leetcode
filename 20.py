
class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        pairset = {"(":")","[":"]","{":"}"}
        candidate = set(['(','[','{'])
        stack = []
        for a in s:
            if len(stack) == 0:
                stack.append(a)
                continue
            else:
                b = stack[-1]
                if b not in candidate:
                    stack.append(a)
                else:
                    if pairset[b] == a:
                        stack.pop()
                    else:
                        stack.append(a)

        if len(stack) == 0:
            return True
        else:
            return False
            
s1 = '()'
s2 = '()[]{}'
s3 = ')}{({))[{{[}'

sol = Solution()
print sol.isValid(s3)