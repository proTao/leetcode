# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # notice use the deep copy
        root = TreeNode(0)
        if(t1 is None and t2 is None):
            return None

        if(t1 is None):
            root.val = t2.val
            root.left = self.mergeTrees(None,t2.left)
            root.right = self.mergeTrees(None, t2.right)
        elif(t2 is None):
            root.val = t1.val
            root.left = self.mergeTrees(None,t1.left)
            root.right = self.mergeTrees(None, t1.right)
        else:
            root.val = t1.val+t2.val
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
        return root

a=TreeNode(5)
b=TreeNode(3)
b.left = a
a=TreeNode(2)
t1=TreeNode(1)
t1.left = b
t1.right = a

a=TreeNode(4)
b=TreeNode(1)
b.right = a
a = TreeNode(7)
c=TreeNode(3)
c.right = a
t2=TreeNode(2)
t2.left=b
t2.right=c

s=Solution()
t3=s.mergeTrees(t1,t2)
print(t3.val,t3.left.val,t3.right.val,t3.left.left.val,t3.left.right.val,t3.right.left,t3.right.right.val)