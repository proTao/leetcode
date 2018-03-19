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
    def connect(self, root):
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
            deeper(root.left)
            deeper(root.right)

        deeper(root, 1)

s = Solution()
