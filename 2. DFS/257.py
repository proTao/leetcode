# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths2(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        print(root and root.val)
        if root is None:
            return []

        return [str(root.val)+"->"+p for p in self.binaryTreePaths(root.left)]+\
                [str(root.val)+"->"+p for p in self.binaryTreePaths(root.right)] or\
                [str(root.val)]

    def binaryTreePaths(self, root):
        res = []
        if root is None:
            return res
        def deeper(path, root):
            if root.left is None and root.right is None:
                res.append(path+str(root.val))
                return

            if root.left:
                deeper(path+str(root.val)+"->",root.left)
            if root.right:
                deeper(path+str(root.val)+"->",root.right)
        deeper("", root)
        return res

t=[TreeNode(1),TreeNode(2),TreeNode(3),TreeNode(5)]
t[0].left = t[1]
t[1].right = t[2]
t[0].right = t[3]

s = Solution()
print(s.binaryTreePaths(t[0]))