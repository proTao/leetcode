# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_depth = 0
        if root is None:
            return 0
        def deeper(node, depth):
            if node.left is None and node.right is None:
                if depth > self.max_depth:
                    self.max_depth = depth 
                return

            if node.left:
                deeper(node.left, depth+1)
            if node.right:
                deeper(node.right, depth+1)

        deeper(root,1)
        return self.max_depth

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None:
            return 0

        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

       


t = [TreeNode(3),TreeNode(9),TreeNode(20),TreeNode(15),TreeNode(7)]
t[0].left = t[1]
t[0].right = t[2]
t[2].left = t[3]
t[2].right = t[4]
s = Solution()
res = s.maxDepth(t[0])
print(res)
