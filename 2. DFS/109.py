from treetools import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        size = 0
        temp = head
        while temp:
            size += 1
            temp = temp.next

            
        self.list_runner = head

        def sortedListToBSTCore(l, r):
            if l == r:
                return None
            mid =  (l+r)//2
            left = sortedListToBSTCore(l,mid)
            root = TreeNode(self.list_runner.val)
            self.list_runner = self.list_runner.next
            root.left = left
            root.right = sortedListToBSTCore(mid+1,r)
            return root

        return sortedListToBSTCore(0,size)

l = [ListNode(i) for i in range(10)]
for i in range(9):
    l[i].next = l[i+1]

t = Solution().sortedListToBST(l[0])
prettyPrintTree(t)