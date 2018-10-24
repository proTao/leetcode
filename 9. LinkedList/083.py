from linkedtools import *

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = head
        while head:
            val = head.val
            while head.next and head.next.val == val:
                head.next = head.next.next
            head = head.next
        return res

a = stringToListNode("[1,1,2,3,3,4]")
prettyPrintLinkedList(Solution().deleteDuplicates(a))