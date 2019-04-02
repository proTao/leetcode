from linkedtools import *

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
    def __repr__(self):
        return str(self.label)+"<"+str(id(self))+">"

class Solution(object):
    def copyRandomList1(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dic1 = {}
        dic2 = {}
        headnode = ListNode(None)
        p = ListNode(None)
        p.next=headnode
        c = ListNode(None)
        c.next = head
        i = 1
        while c.next:
            p.next.next = RandomListNode(c.next.label)
            p.next = p.next.next
            dic1[c.next] = i
            dic2[i] = p.next
            c.next = c.next.next
            i += 1
        c = headnode.next
        print(dic1, dic2)
        while head:
            if head.random:
                index = dic1[head.random]
                c.random = dic2[index]
            head = head.next
            c = c.next
        print("0k0k0")
        return headnode.next

    def copyRandomList(self, head):
        # O(1) space complexity
        # O(n) time complexity
        if head is None:
            return head
        # round 1: create shadow chain
        p = head
        while p:
            p2 = p.next
            p.next = RandomListNode(p.label)
            p.next.next = p2
            p = p2
        head2 = head.next

        # round 2: handle random link of shadow chain 
        p = head
        while p:
            if p.random is not None:
                p.next.random = p.random.next
            p = p.next.next
        
        # round 3: split origin chain and shadow chain
        p = head
        while p.next.next:
            p2 = p.next.next
            p.next.next = p2.next
            p.next = p2
            p = p2
        p.next=None

        return head2

a1 = RandomListNode('a')
a2 = RandomListNode('b')
a3 = RandomListNode('c')
a4 = RandomListNode('d')
a5 = RandomListNode('e')
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
a1.random = a3
a3.random = a2
a4.random = a2
a5.random = a5
head = a1
while head:
    print(head.label, head.random)
    head = head.next

head = Solution().copyRandomList(a1)
while head:
    print(head.label, head.random)
    head = head.next
