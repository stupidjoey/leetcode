class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.stackarr = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stackarr.append(x)
        

    # @return nothing
    def pop(self):
        if self.empty():
            pass
        else:
            num = len(self.stackarr)-1
            for i in range(num):
                temp = self.stackarr[0]
                self.popfront()
                self.push(temp)
            self.popfront()
            
    def popfront(self):
        if self.empty():
            pass
        else:
            self.stackarr[0:1] = []

    # @return an integer
    def top(self):
        if self.empty():
            return None
        else:
            num = len(self.stackarr)-1
            for i in range(num):
                temp = self.stackarr[0]
                self.popfront()
                self.push(temp)
            topval = self.stackarr[0]
            self.popfront()
            self.push(topval)
            return topval
        

    # @return an boolean
    def empty(self):
        if len(self.stackarr) == 0:
            return True
        else:
            return False
        