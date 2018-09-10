from collections import deque
class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()
        self.length = 0


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if self.q1:
            self.q1.append(x)
        else:
            self.q2.append(x)
        self.length += 1
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.q1:
            l = self.length
            while l > 1:
                l -= 1
                self.q2.append(self.q1.popleft())
            self.length -= 1
            return self.q1.popleft()
        else:
            l = self.length
            while l > 1:
                l -= 1
                self.q1.append(self.q2.popleft())
            self.length -= 1
            return self.q2.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.q1:
            l = self.length
            while l > 1:
                l -= 1
                self.q2.append(self.q1.popleft())
            res = self.q1.popleft()
            self.q2.append(res)
            return res
        else:
            l = self.length
            while l > 1:
                l -= 1
                self.q1.append(self.q2.popleft())
            res = self.q2.popleft()
            self.q1.append(res)
            return res
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.length == 0


stack = MyStack()

stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.empty())