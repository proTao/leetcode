from linkedtools import *

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while not slow is fast:
            if slow:
                slow = slow.next
            else:
                return False
            if fast and fast.next:
                fast = fast.next.next
            else:
                return False
        return True

a = stringToListNode("[1,2,3,4]")
a.next.next.next.next = a.next
print(Solution().hasCycle(a))