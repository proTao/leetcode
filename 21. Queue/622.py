class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.data = [None] * k
        self.head = 0
        self.tail = 0
        self.capacity = k
        self.size = 0
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. 
        Return true if the operation is successful.
        """
        if self.size == self.capacity:
            return False
        self.data[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. 
        Return true if the operation is successful.
        """
        if self.size == 0:
            return False
        self.data[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.data[self.head] if self.size else -1


    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.size:
            return self.data[(self.tail + self.capacity - 1)%self.capacity]
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == self.capacity

if __name__ == "__main__":
    obj = MyCircularQueue(2)
    print(obj.enQueue(1))
    print(obj.enQueue(2))
    print(obj.enQueue(3))
    print(obj.deQueue())
    print(obj.Front())
    print(obj.Rear())
    print(obj.isEmpty())
    print(obj.isFull())