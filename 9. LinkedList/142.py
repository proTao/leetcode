from linkedtools import ListNode, prettyPrintLinkedList, stringToListNode
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None
        fast = head.next.next
        slow = head.next

        while not fast is slow:
            try:
                slow = slow.next
                fast = fast.next.next
            except AttributeError:
                return None
        
        fast = head
        while not fast is slow:
            slow, fast = slow.next, fast.next
        return slow

a = stringToListNode("[1,2,3,4,5]")
a.next.next.next.next = a.next
print(Solution().detectCycle(a).val)