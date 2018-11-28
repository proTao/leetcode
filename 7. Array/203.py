class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """




        # if is the first node
        while head and head.val == val:
            head = head.next
        if not head:
            return head
        # if not
        forward = head
        later = head.next
        while later:
            # print(later.val)
            if later.val == val:
                forward.next = later.next
                later = later.next
            else:
                forward = later
                later = later.next
        return head

# environment
a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(2)
a5 = ListNode(1)
# a1.next = a2
# a2.next = a3
# a3.next = a4
# a4.next = a5

# my solution

s = Solution()
res = s.removeElements(a1,1)

# end of my solution

while(1):
    if(res):
        print(res.val)
        res = res.next
    else:
        break

print("end")