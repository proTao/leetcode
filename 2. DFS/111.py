# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None :
            return 0
        if root.left is None and root.right is None:
            return 1

        if root.left is None:
            return 1+self.minDepth(root.right)
        if root.right is None:
            return 1+self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    def minDepth(self, root):
        self.min_depth = 10000000
        if root == None:
            return 0

        def deeper(root, current_depth):
            print(root.val)
            if root.left == None and root.right == None:
                if current_depth < self.min_depth:
                    self.min_depth = current_depth
                return

            if current_depth + 1 < self.min_depth:
                if root.left:
                    deeper(root.left, current_depth+1)
                if root.right:
                    deeper(root.right, current_depth+1)

        deeper(root, 1)
        return self.min_depth


print("res",Solution().minDepth(stringToTreeNode("[1,null,2]")))