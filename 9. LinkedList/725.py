from linkedtools import ListNode, stringToListNode, prettyPrintLinkedList
class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        length = 0
        current = root
        while current:
            length += 1
            current = current.next
        single_length, rest = divmod(length, k)
        print(single_length, rest)
        res = []
        
        current = root
        j = 0
        while j < k:
            i = 1
            res.append(current)
            while i < single_length:
                current = current.next
                i += 1
            if rest and single_length >= 1:
                current = current.next
                rest -= 1
            if current:
                temp = current.next
                current.next  = None
                current = temp
            prettyPrintLinkedList(res[j])
            j += 1
        return res

s = Solution()
a = stringToListNode("[1,2,3]")
res = s.splitListToParts(a, 2)