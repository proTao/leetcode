from treetools import *

class Solution:
    def tree2str(self, t:TreeNode):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ""

        def deeper(t: TreeNode, res: list):
            if t.right:
                r = ["(", self.tree2str(t.right), ")"]
            else:
                r = [""]
            if t.left:
                l = ["(", self.tree2str(t.left), ")"]
            else:
                if t.right:
                    l = ["()"]
                else:
                    l = [""]

            res.append(str(t.val))
            res.extend(l)
            res.extend(r)
        res = []
        deeper(t, res)
        return "".join(res)

t = stringToTreeNode("[1,2,3,null,4]")
print(Solution().tree2str(t))
            
        
        