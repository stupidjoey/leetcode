class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        stack = []
        pathset = path.split('/')
        for p in pathset:
            if p == '':
                pass
            elif p == '.':
                pass
            elif p == '..':
                if len(stack) > 0:
                    stack.pop()
                else:
                    pass
            else:
                stack.append(p)
        
        simple_path = ''
        if len(stack) > 0:
            for p in stack:
                simple_path += '/' + p
            return simple_path
        else:
            return '/'
            
            