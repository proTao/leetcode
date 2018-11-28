from linkedtools import *
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
            
        if l1.val <= l2.val:
            head = l1
            node1 = l1.next
            node2 = l2
        else:
            head = l2
            node1 = l1
            node2 = l2.next

        current = head
        while node1 and node2:
            if node1.val < node2.val:
                current.next = node1
                current, node1 = node1, node1.next
            else:
                current.next = node2
                current, node2 = node2, node2.next
        if node1:
            current.next = node1
        else:
            current.next = node2
        return head

l1 = stringToListNode("[1,2,4]")
prettyPrintLinkedList(l1)
l2 = stringToListNode("[1,3,4]")
prettyPrintLinkedList(l2)
prettyPrintLinkedList(Solution().mergeTwoLists(l1,l2))
                
            