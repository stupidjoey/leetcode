class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
    

        def recursive(n):
            if n == 1:
                return ["()"]
            else:
                finalcases = []
                basecases = self.generateParenthesis(n-1).split(',')
                for case in basecases:
                    newcase1 = "()" + case
                    newcase2 = case + "()"
                    newcase3 = "(" + case + ")"
                    finalcases.append(newcase1)
                    finalcases.append(newcase2)
                    finalcases.append(newcase3)
                finalcases = list(set(finalcases))
                return finalcases
                
        finalcases = recursive(n)
        finalstr = ''
        for case in finalcases:
            print case
        return finalstr[:-1]
    
sol = Solution()

print repr(sol.generateParenthesis(3))