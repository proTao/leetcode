from treetools import *
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect2(self, root):
        # use None to holdplace to make sure the top layer is layer 1
        self.cache = [None,]

        def deeper(root, depth):
            if root is None:
                return
            if depth == len(self.cache):
                self.cache.append(root)
            else:
                self.cache[depth].next = root
                self.cache[depth] = root
            deeper(root.left, depth+1)
            deeper(root.right, depth+1)

        deeper(root, 1)

    def connect(self, root):
        if root is None:
            return

        if root.left and root.right:
            l = root.left
            r = root.right
            while l and r:
                print(l.val, r.val)
                l.next = r
                l = l.right or l.left
                r = r.left or r.right

        self.connect(root.left)
        self.connect(root.right)

    def connect3(self, root):
        while root:
            cur = tmp = TreeLinkNode(0)
            while root:
                if root.left:
                    cur.next = root.left
                    cur = cur.next
                if root.right:
                    cur.next = root.right
                    cur = cur.next
                root = root.next
            root = tmp.next

s = Solution()
t = stringToTreeNode("{1,2,3,4,5,null,6,7,null,null,null,null,8}")
prettyPrintTree(t)
s.connect(t)
# print(t.left.right.next.val)