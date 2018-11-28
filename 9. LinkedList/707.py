from linkedtools import prettyPrintLinkedList, ListNode
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.headnode = ListNode(None)
        self.length = 0
        self.tail = None
        

    def _get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index >= self.length:
            return ListNode(-1)
        else:
            c = self.headnode.next
            for _ in range(index):
                c = c.next
            return c

    def get(self, index):
        return self._get(index).val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        newnode = ListNode(val)
        newnode.next, self.headnode.next = self.headnode.next, newnode
        if self.length == 0:
            self.tail = newnode
        self.length += 1


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        newnode = ListNode(val)
        if self.tail:
            self.tail.next = newnode
        else: # the first node
            self.headnode.next = newnode
        self.tail = newnode
        self.length += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the end of linked list. 
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            insert_point = self._get(index)
            newnode = ListNode(insert_point.val)
            newnode.next = insert_point.next
            insert_point.next = newnode
            insert_point.val = val
            self.length += 1
            if insert_point is self.tail:
                self.tail = insert_point.next
        
        
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if 0 <= index < self.length:
            c = self.headnode
            for _ in range(index):
                c = c.next
            c.next = c.next.next
            if index == self.length - 1:
                self.tail = c
            self.length -= 1
    
    def show(self):
        prettyPrintLinkedList(self.headnode)
            

        


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(0)
obj.addAtIndex(1,9)
obj.addAtIndex(1,5)
obj.addAtTail(7)
obj.show()
obj.addAtHead(1)
obj.show()
obj.addAtIndex(5,8)
obj.addAtIndex(5,2)
obj.addAtIndex(3,0)
obj.addAtTail(1)
obj.addAtTail(0)
obj.show()
# obj.deleteAtIndex(6)