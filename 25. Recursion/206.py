class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        def core(head):
            # 返回翻转后的链表的头和尾
            if head.next is None:
                return head, head
            reversed_head, reversed_tail = core(head.next)
            reversed_tail.next = head
            head.next = None
            return reversed_head, head

        return core(head)[0]