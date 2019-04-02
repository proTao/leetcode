from linkedtools import *
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head
        headnode = ListNode(0)
        headnode.next = head
        p = headnode
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next

        return headnode.next

if __name__ == "__main__":
    a = stringToListNode("[1,2,3,6,4,5,6]")
    prettyPrintLinkedList(Solution().removeElements(a, 6))