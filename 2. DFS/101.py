# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        def deeper(left, right):
            if left is None or right is None:
                return left == right

            return deeper(left.left, right.right) and \
                    deeper(left.right, right.left) and \
                    left.val == right.val

        return deeper(root.left, root.right)

t = [TreeNode(1),TreeNode(2),TreeNode(2),TreeNode(3),TreeNode(4),TreeNode(4),TreeNode(3),TreeNode(1)]
t[0].left = t[1]
t[0].right = t[3]

# t[1].left = t[3]
# t[1].right = t[4]
# t[2].left = t[5]
# t[2].right = t[6]
# t[6].right = t[7]
s = Solution()
print(s.isSymmetric(t[0]))