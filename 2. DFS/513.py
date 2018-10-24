from treetools import *


class Solution:
    def findBottomLeftValue2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # backtrack
        self.max_depth = 0
        self.bottom_left_value = -1

        def deeper(root, depth):
            # return condition: leave node
            if root.left is None and root.right is None:
                if depth > self.max_depth:
                    self.bottom_left_value = root.val
                    self.max_depth = depth

            if root.left:
                deeper(root.left, depth+1)

            if root.right:
                deeper(root.right, depth+1)

        deeper(root, 1)
        return self.bottom_left_value

    def findBottomLeftValue(self, root):
        # dfs by Post order
        def dfsPostOrder(root):
            # print(root.val)
            if root.left is None and root.right is None:
                print("return")
                return (1, root.val)


            res_l = None
            res_r = None
            if root.left is not None:
                res_l = dfsPostOrder(root.left)

            if root.right is not None:
                res_r = dfsPostOrder(root.right)

            # print(root.val,res_l,res_r)
            print((res_r is None) and (res_l[0]+1, res_l[1]))
            res = ((res_l is None) and (res_r[0]+1, res_r[1])) or\
                    ((res_r is None) and (res_l[0]+1, res_l[1])) or\
                    ((res_r[0]+1, res_r[1]) if res_r[0]>res_l[0] else (res_l[0]+1, res_l[1]))
            return res

        return dfsPostOrder(root)[1]



t = stringToTreeNode("[1,2,3,4,null,5,6,null,null,7]")
prettyPrintTree(t)
print(Solution().findBottomLeftValue(t))