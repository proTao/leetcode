from treetools import *

class Solution:
    def isSubtree(self, s:TreeNode, t:TreeNode) -> bool:

        def deeper(s:TreeNode, t:TreeNode) -> bool:            
            if s and t is None or t and s is None:
                return False
            if s is None and t is None:
                return True

            # both not none
            print("-------------------------")
            prettyPrintTree(s)
            prettyPrintTree(t)
            if s.val == t.val:
                return sameTree(s.left, t.left) and sameTree(s.right, t.right)\
                        or deeper(s.left, t) or deeper(s.right, t)
            else:
                return deeper(s.left, t) or deeper(s.right, t)

        def sameTree(s:TreeNode, t:TreeNode) -> bool:
            if s and t is None or t and s is None:
                return False
            if s is None and t is None:
                return True

            # both not none
            if s.val != t.val:
                return False
            else:
                return sameTree(s.left, t.left) and sameTree(s.right, t.right)


        return deeper(s, t)


s = stringToTreeNode("[3,4,5,1,null,2]")
t = stringToTreeNode("[3,1,2]")
prettyPrintTree(s)
prettyPrintTree(t)
print(Solution().isSubtree(s,t))