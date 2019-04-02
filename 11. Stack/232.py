class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.length = 0

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)
        self.length += 1

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.empty():
            return None
        self.length -= 1

        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
        
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.stack2:
            return self.stack2[-1]
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0


q = MyQueue()
# ["MyQueue","push","push","push","pop","pop","pop","empty"]
# [[],[1],[2],[3],[],[],[],[]]
q.push(1)
q.push(2)
q.push(3)
print(q.pop())
print(q.pop())
print(q.pop())