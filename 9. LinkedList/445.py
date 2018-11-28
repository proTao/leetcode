from linkedtools import ListNode, stringToListNode, prettyPrintLinkedList
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        c = l1
        while c:
            num1 = num1 * 10 + c.val
            c = c.next
        num2 = 0
        c = l2
        while c:
            num2 = num2 * 10 + c.val
            c = c.next
        res = str(num1 + num2)
        head = ListNode(int(res[0]))
        c = head
        for i in res[1:]:
            newnode = ListNode(int(i))
            c.next = newnode
            c = newnode
        return head

a = stringToListNode("[0]")
b = stringToListNode("[0]")
prettyPrintLinkedList(Solution().addTwoNumbers(a,b))

        