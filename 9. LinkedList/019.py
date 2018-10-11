from linkedtools import stringToListNode, prettyPrintLinkedList
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        target = length - n
        if target == 0:
            return head.next
        else:
            node = head
            for i in range(target-1):
                node = node.next
            node.next = node.next.next
            return head

a = stringToListNode("[1,2,3,4,5]")
prettyPrintLinkedList(Solution().removeNthFromEnd(a, 5))
