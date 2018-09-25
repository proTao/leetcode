# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from random import randrange
class Solution:

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        c = head
        length = 0
        while c:
            length += 1
            c = c.next
        self.length = length

        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        c = self.head
        rand_index = randrange(0, self.length)
        while rand_index:
            c = c.next
            rand_index -= 1
        return c.val


# Your Solution object will be instantiated and called as such:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
obj = Solution(head)

for i in range(10):
    print(obj.getRandom())