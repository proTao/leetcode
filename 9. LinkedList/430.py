from linkedtools import prettyPrintLinkedList
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
class Solution(object):
    def flatten(self, head:Node):
        """
        :type head: Node
        :rtype: Node
        """
        stack = []
        res = head
        c = head
        prev = None
        while stack or c:
            if c is None:
                c = stack.pop()
                prev.next = c
                c.prev = prev

            if c.child:
                if c.next:
                    stack.append(c.next)
                c.next = c.child
                c.next.prev = c
                c.child = None
            prev = c
            c = c.next
        return res
