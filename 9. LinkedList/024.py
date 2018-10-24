from linkedtools import ListNode, prettyPrintLinkedList, stringToListNode
class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        c = head
        while True:
            if c and c.next:
                c.val, c.next.val = c.next.val, c.val
                c = c.next.next
            else:
                break
        return head

a = stringToListNode("[]")
prettyPrintLinkedList(Solution().swapPairs(a))