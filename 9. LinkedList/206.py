from linkedtools import *

class Solution:
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        first, second, third = head, head.next, head.next.next
        first.next = None
        
        while True:
            second.next = first
            if third is None:
                return second
            first, second, third = second, third, third.next
    
    def reverseList(self, head):
        if head is None:
            return head
        if head.next is None:
            return head
        p = head
        while p.next:
            p2 = p.next
            p.next = p2.next
            p2.next = head
            head = p2
        return head
        
prettyPrintLinkedList(Solution().reverseList(stringToListNode("[1,2,3]")))