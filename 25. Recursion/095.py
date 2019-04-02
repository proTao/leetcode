from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        def core(n, base):
            if n == 0:
                return [None]
            if n == 1:
                return [TreeNode(base)]
            res = []
            for leftnodes in range(0, n):
                lefttrees = core(leftnodes,base)
                righttrees = core(n-1-leftnodes, base+leftnodes+1)
                for left_t in lefttrees:
                    for right_t in righttrees:
                        root = TreeNode(leftnodes+base)
                        root.left = left_t
                        root.right = right_t
                        res.append(root)
            return res
        return core(n, 1)