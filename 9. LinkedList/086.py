from linkedtools import *
class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        head1 = ListNode(None)
        head2 = ListNode(None)
        p1 = head1
        p2 = head2
        while head:
            if head.val < x:
                p1.next = head
                p1 = head
            else:
                p2.next = head
                p2 = head
            head = head.next
        if p1.next:
            p1.next = None
        if p2.next:
            p2.next = None
        p1.next = head2.next
        return head1.next
s = stringToListNode("[1,4,2,3,5,2]")
prettyPrintLinkedList(Solution().partition(s,3))