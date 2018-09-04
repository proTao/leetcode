from linkedtools import *

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        def reverse_L(head, k):
            if head is None or head.next is None:
                return head
            length = 0
            p = head
            while p and length < k:
                p = p.next
                length += 1
            if length < k:
                return head
                
            
            a = head
            b = a.next
            c = b.next
            i = 2
            while i < k and c:
                b.next = a
                a, b, c = b, c, c.next
                i += 1
            head.next = reverse_L(b.next, k)
            b.next = a
            
            return b
        return reverse_L(head, k)
        
a = stringToListNode("[1,2]")
prettyPrintLinkedList(Solution().reverseKGroup(a, 3))