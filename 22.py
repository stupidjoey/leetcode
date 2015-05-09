class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        if n == 1:
            return ['()']
        else:
            finalcases = []
            halfn = n/2
            for i in range(1,halfn+1):
                j = n - i
                basecases_i = self.generateParenthesis(i)
                basecases_j = self.generateParenthesis(j)
                for casei in basecases_i:
                    for casej in basecases_j:
                        newcase1 = casei + casej
                        newcase2 = casej + casei
                        finalcases.append(newcase1)
                        finalcases.append(newcase2)
                        if i == 1:
                            newcase3 = "(" + casej + ")"
                            finalcases.append(newcase3)
            finalcases = list(set(finalcases))
            return finalcases
                

sol = Solution()

print repr(sol.generateParenthesis(4))
