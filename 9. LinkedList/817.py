from linkedtools import *

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        G = set(G)
        components = 0
        new_component = True
        while head:
            if head.val in G:
                if new_component:
                    components += 1
                    new_component = False
            else:
                new_component = True
            head = head.next
        return components   

a = stringToListNode("[1,2,3,4,5]")
G = [1,2,3,4]
print(Solution().numComponents(a, G))
