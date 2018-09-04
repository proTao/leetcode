from linkedtools import ListNode, prettyPrintLinkedList, stringToListNode
class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        head1 = head
        head2 = head.next
        c1 = head1
        c2 = head2
        while c2 and c2.next:
            c1.next = c2.next
            c1 = c1.next
            c2.next = c1.next
            c2 = c2.next
        c1.next = head2
        return head1

a = stringToListNode("[]")
prettyPrintLinkedList(Solution().oddEvenList(a))
        