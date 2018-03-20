from math import log10
from treetools import *

class Solution:
    def sumNumbers(self, root):
        self.res = 0
        if root is None:
            return 0
        def deeper(root, prefix):
            # print(root and root.val, prefix)
            if root.left is None and root.right is None:
                self.res += prefix*10+root.val
                return

            root.left and deeper(root.left, prefix*10+root.val)
            root.right and deeper(root.right, prefix*10+root.val)
        deeper(root,0)
        return self.res


    def sumNumbers1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        def sumNumbersCore(root):
            if root.left is None and root.right is None:
                return [root.val]

            l = root.left and sumNumbersCore(root.left) or []
            r = root.right and sumNumbersCore(root.right) or []
            print(root.val,l,r)
            return [root.val*10**int((log10(i) if i!=0 else 0)//1+1) + i for i in l+r]

        return sum(sumNumbersCore(root))

t = stringToTreeNode("[]")
prettyPrintTree(t)
print(Solution().sumNumbers(t))