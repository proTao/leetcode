# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p and p.val) != (q and q.val):
            return False

        # p q are both None or have same value
        return (q == None) or \
                (self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right))