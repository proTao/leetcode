class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs1(self, head: ListNode) -> ListNode:
        if head:
            if head.next:
                head.val, head.next.val = head.next.val, head.val
                self.swapPairs1(head.next.next)

        return head
    
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        second = head.next
        head.next = self.swapPairs(second.next)
        second.next = head
        return second