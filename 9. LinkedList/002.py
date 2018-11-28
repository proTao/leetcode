from linkedtools import ListNode, prettyPrintLinkedList, stringToListNode

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        bonus = 0
        c = l1
        len1 = 0
        while c:
            len1 += 1
            c = c.next
        c = l2
        len2 = 0
        while c:
            len2 += 1
            c = c.next
        if len1 < len2:
            l1, l2 = l2, l1
        prettyPrintLinkedList(l1)
        prettyPrintLinkedList(l2)
        res = l1
        while l2:
            bonus, l1.val = divmod(l1.val+l2.val+bonus, 10)
            last = l1
            l1 = l1.next
            l2 = l2.next
        while bonus and l1:
            bonus, l1.val = divmod(l1.val+bonus, 10)
            last = l1
            l1 = l1.next
        if bonus:
            last.next = ListNode(1)
        return res

a = stringToListNode("[5]")
b = stringToListNode("[5]")
prettyPrintLinkedList(Solution().addTwoNumbers(a,b))
        