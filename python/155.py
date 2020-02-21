class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minima = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if self.minima is None:
            self.minima = x
        else:
            if x < self.minima:
                self.minima = x

    def pop(self):
        """
        :rtype: None
        """
        val = self.stack.pop()
        if val == self.minima:
            nminima = None
            for ele in self.stack:
                if nminima is None:
                    nminima = ele
                else:
                    if ele < nminima:
                        nminima = ele
            self.minima = nminima

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minima


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
