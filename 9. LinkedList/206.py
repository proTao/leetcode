from linkedtools import *

class Solution:
    def reverseList(self, head):
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
        
        
prettyPrintLinkedList(Solution().reverseList(stringToListNode("[1,2]")))