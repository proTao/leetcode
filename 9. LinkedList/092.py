from linkedtools import ListNode, stringToListNode, prettyPrintLinkedList

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or head.next is None or m == n:
            return head
        headnode = ListNode(-1)
        headnode.next = head
        anchor = headnode
        for _ in range(m-1):
            anchor = anchor.next
        a = anchor.next
        b = a.next
        c = b.next

        k = n - m
        for _ in range(k):
            b.next = a
            if c:
                a, b, c = b, c, c.next
            else:
                a, b = b, c 
        anchor.next.next = b
        anchor.next = a
        return headnode.next
    
a = stringToListNode("[1,2,3]")
prettyPrintLinkedList(Solution().reverseBetween(a, 2, 3))


