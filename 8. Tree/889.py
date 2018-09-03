from treetools import *

class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """

        def split(A, B):
            rightest_of_L = -1
            length_of_L = 0
            for i,x in enumerate(A):
                rightest_of_L = max(rightest_of_L, B.index(x)+1)
                length_of_L += 1
                if rightest_of_L == length_of_L and A[0] == B[i]:
                    return length_of_L
        
        def core(pre, post):
            node = TreeNode(pre[0])
            if len(pre) == 1:
                return node
            else:
                length_L = split(pre[1:], post[:-1])
                node.left = core(pre[1:1+length_L], post[:length_L])
                if len(pre)-1-length_L > 0:
                    node.right = core(pre[1+length_L:], post[length_L:-1])
                return node
        return core(pre, post)
    
pre = [1,2,4,5,3,6,7]
post = [4,5,2,6,7,3,1]
prettyPrintTree(Solution().constructFromPrePost(pre, post))
        


