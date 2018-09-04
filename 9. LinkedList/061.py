from linkedtools import *
class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next
        k = k % length
        p = head
        for _ in range(length - k - 1):
            p = p.next
        tail.next = head
        res = p.next
        p.next = None

        return res
        

a = stringToListNode("[1,2,3,4,5,6,7]")
prettyPrintLinkedList(Solution().rotateRight(a,1))