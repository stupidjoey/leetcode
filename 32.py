class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        s_len = len(s)
        if s_len == 0:
            return 0
        stack = []
        idx_stack = []
        for idx in range(s_len):
            c = s[idx]
            if len(stack) > 0:
                if stack[-1] == '(' and c == ')':
                    stack.pop()
                    idx_stack.pop()
                    continue
            stack.append(c)
            idx_stack.append(idx)
        idx_stack.insert(0,-1)
        idx_stack.append(s_len)
        max_count = 0
        for i in range(1,len(idx_stack)):
            tempcount = idx_stack[i] - idx_stack[i-1] - 1
            max_count = max(max_count, tempcount)
        return max_count
            
            
 