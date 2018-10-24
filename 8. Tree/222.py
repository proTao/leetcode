from treetools import *

class Solution1:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        right_depth = 0
        left_depth = 0
        node = root
        while node:
            node = node.right
            right_depth += 1
        node = root
        while node:
            node = node.left
            left_depth += 1
        if left_depth == right_depth:
            return 2 ** left_depth - 1

        self.right_depth = right_depth
        self.left_depth = left_depth
        self.high_count = 0
        self.stop_flag = False
        self.half = False
        self.count = 0

        def dfs(root, depth):
            self.count += 1
            if depth == self.left_depth:
                self.stop_flag = True
            if root.left is None and root.right is None:
                if depth == self.right_depth:
                    self.high_count += 1
            elif root.right is None:
                self.half = True
            else:
                if self.stop_flag:
                    return
                dfs(root.right, depth + 1)
                dfs(root.left, depth + 1)
        dfs(root, 1)
        print(self.high_count, self.half, self.left_depth, self.right_depth, self.count)
        lower_leaves = 2*(2 ** (self.right_depth-1) - self.high_count)
        
        if self.half:
            lower_leaves -= 1
        print(lower_leaves)
        return 2 ** self.right_depth - 1 + lower_leaves

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left_depth, right_depth = self.getLLength(root), self.getRLength(root)
        def dfs(root, left_depth, right_depth):
            print(left_depth, right_depth)
            if left_depth == right_depth:
                return 2**left_depth - 1 if left_depth > 0 else 0
            else:
                left_right_depth = self.getRLength(root.left)
                right_left_depth = self.getLLength(root.right)
                left_node = dfs(root.left, left_depth-1, left_right_depth)
                right_node = dfs(root.right, right_left_depth, right_depth-1)

                return left_node + right_node + 1

        return dfs(root, left_depth, right_depth)

    def getLLength(self, root):
        if root is None: return 0
        left_depth = 0
        node = root
        while node: node, left_depth = node.left, left_depth + 1
        return left_depth

    def getRLength(self, root):
        if root is None: return 0
        right_depth = 0
        node = root
        while node: node, right_depth = node.right, right_depth+1
        return right_depth

t = stringToTreeNode(str([i for i in range(700)]))
print(Solution().countNodes(t))
