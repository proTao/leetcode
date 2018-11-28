from linkedtools import *

class Solution:
    def reorderList(self, head:ListNode):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # boundary
        if head is None or head.next is None:
            return

        # find half
        length = 0
        c = head
        while c:
            c = c.next
            length += 1
        a = head
        for _ in range((length+1)//2-1):
            a = a.next

        
        # flip laster half
        # cut
        temp = a.next
        a.next = None
        a = temp
        del temp
        # flip
        if a.next:
            b = a.next # not None
            a.next = None 
            c = b.next # maybe None
            while c:
                b.next = a
                a, b, c = b, c, c.next
            b.next = a
        else:
            b = a
        del c

        # reorder
        # now node b is the first node of the flipped half chain
        a = head
        # prettyPrintLinkedList(a)
        # prettyPrintLinkedList(b)
        while b:
            a_ = a.next
            a.next = b
            a = a_
            b_ = b.next
            b.next = a
            b = b_

a = stringToListNode("[1,2,3,4,5,6]")
prettyPrintLinkedList(Solution().reorderList(a))


        