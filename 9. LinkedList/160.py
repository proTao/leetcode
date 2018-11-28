from linkedtools import *
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        tailA = headA
        lengthA = 1
        while tailA and tailA.next:
            tailA = tailA.next
            lengthA += 1
        tailB = headB
        lengthB = 1
        while tailB and tailB.next:
            tailB = tailB.next
            lengthB += 1
        if not tailA is tailB:
            return None
        if lengthA > lengthB:
            i = 0
            while i + lengthB < lengthA:
                headA = headA.next
                i += 1
        if lengthA < lengthB:
            i = 0
            while i + lengthA < lengthB:
                headB = headB.next
                i += 1
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA

a = stringToListNode("[1,2,3]")
b = a.next
print(Solution().getIntersectionNode(a,b).val)