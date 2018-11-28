from treetools import *

class Solution:
    def rightSideView(self, root):
        #M1: Depth-First Search (DFS)
        rightmost_value_at_depth = {} # dictny is pairs of (mostRightValue, itsdepth)
        max_depth = -1

        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()

            if node is not None:
                # maintain knowledge of the number of levels in the tree.
                max_depth = max(max_depth, depth)

                # only insert into dict if depth is not already present.
                rightmost_value_at_depth.setdefault(depth, node.val)

                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth+1)]
    def rightSideView2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root is None:
            return []

        def deeper(root, depth):
            if depth > len(res):
                res.append(root.val)

            root.right and deeper(root.right, depth+1)
            root.left and deeper(root.left, depth+1)
        deeper(root, 1)
        return res

t = stringToTreeNode("[1,2,3,4,5,6, null,7]")
prettyPrintTree(t)
print(Solution().rightSideView(t))