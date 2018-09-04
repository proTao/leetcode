from linkedtools import ListNode, prettyPrintLinkedList, stringToListNode

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        headnode = ListNode(None)
        headnode.next = head
        delete = False
        p = headnode # prev
        c = head # current
        while c:
            while c.next and c.val == c.next.val:
                c.next = c.next.next
                if not delete:
                    delete = True
            if delete:
                c = c.next
                p.next = c
                delete = False
            else:
                c = c.next
                p = p.next
        return headnode.next

a = stringToListNode("[1,1,1,2,2,4]")
prettyPrintLinkedList(Solution().deleteDuplicates(a))

            
