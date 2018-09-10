class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.length = 0
        self.data_stack = []
        self.min_index = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.length == 0 or self.data_stack[self.min_index[-1]] > x:
            self.min_index.append(self.length)
        self.length += 1
        self.data_stack.append(x)
        


    def pop(self):
        """
        :rtype: void
        """
        self.length -= 1
        if self.length == self.min_index[-1]:
            self.min_index.pop()
        self.data_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.data_stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.data_stack[self.min_index[-1]]
        
s = MinStack()
s.push(-2)
s.push(0)
s.push(-1)
print(s.getMin())
print(s.pop())
print(s.top())
print(s.getMin())