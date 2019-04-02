from linkedtools import ListNode, stringToListNode, prettyPrintLinkedList
class Solution:
    def addTwoNumbers(self, l1, l2):
        headnode = ListNode(0)
        p = headnode
        p1, p2 = l1, l2
        carry = 0

        # 处理等长部分
        while p1 and p2:
            val = p2.val+p1.val+carry
            p.next = ListNode(val%10)
            carry = val//10
            p, p1, p2 = p.next, p1.next, p2.next

        # 处理不等长的部分
        while p1:
            val = p1.val+carry
            p.next = ListNode(val%10)
            carry = val//10
            p, p1 = p.next, p1.next
        while p2:
            val = p2.val+carry
            p.next = ListNode(val%10)
            carry = val//10
            p, p2 = p.next, p2.next

        if carry > 0:
            p.next = ListNode(carry)

        return headnode.next



a = stringToListNode("[1,8]")
b = stringToListNode("[0]")
prettyPrintLinkedList(Solution().addTwoNumbers(a,b))

        