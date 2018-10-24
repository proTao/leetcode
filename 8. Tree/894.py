from treetools import *

class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        fbt_n = [[], [TreeNode(0)],[]]
        if N <= 2:
            return fbt_n[N]
        for i in range(3, N+1):
            print(i)
            temp_res = []
            for left in range(1, i-1):
                right = i-1-left
                for lefttree in fbt_n[left]:
                    for righttree in fbt_n[right]:
                        temp_res.append(TreeNode(0))
                        temp_res[-1].left = lefttree
                        temp_res[-1].right = righttree
            fbt_n.append(temp_res)
        return fbt_n[-1]

for t in Solution().allPossibleFBT(7):
    prettyPrintTree(t)

