from linkedtools import *
class Solution(object):
    def isPalindrome(self, head):
        if head is None:
            return True
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        half_length = (length + 1)//2
        half = head
        while half_length:
            half = half.next
            half_length -= 1
        
        def reverseList(head):
            if head is None or head.next is None:
                return head
            first, second, third = head, head.next, head.next.next
            first.next = None
            while True:
                second.next = first
                if third is None:
                    return second
                first, second, third = second, third, third.next
        half = reverseList(half)
        while head and half:
            if head.val != half.val:
                return False
            head = head.next
            half = half.next
        return True
        
    

        
a = stringToListNode("[1,2,1]")
s = Solution()
print(s.isPalindrome(a))