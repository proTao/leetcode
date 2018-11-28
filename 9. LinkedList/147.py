from linkedtools import prettyPrintLinkedList, stringToListNode, ListNode
class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        sorted = head
        unsorted = head.next
        inf = ListNode(float("inf"))
        sorted.next = inf
        # sorted.next.next = sorted
        
        while unsorted:
            c = sorted
            while c.val < unsorted.val:
                c = c.next
            temp = unsorted
            unsorted = unsorted.next
            
            temp.next = c.next
            c.next = temp
            c.val, temp.val = temp.val, c.val
            
        while True:
            if c.next.val == float("inf"):
                break
            c = c.next
        c.next = None
        return sorted

a = stringToListNode("[6,5,3,1,8,7,2,4]")
# a = stringToListNode("[1,6]")
prettyPrintLinkedList(Solution().insertionSortList(a))