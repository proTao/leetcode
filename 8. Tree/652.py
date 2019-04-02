from treetools import *

None_hash = 812363
left_coef = 129379
right_coef = 864119
current_coef = 123983
class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.hashset = set([])
        self.used = set([])
        # self.used.add(None_hash)
        self.res = set()
        def hashTree(root):
            if root is None:
                return None_hash
            left_hash = hashTree(root.left)
            right_hash = hashTree(root.right)
            current_hash = (root.val * current_coef + left_hash * left_coef + right_hash * right_coef)
            if current_hash in self.hashset:
                if current_hash not in self.used:
                    self.res.add(root)
                    self.used.add(current_hash)
            else:
                self.hashset.add(current_hash)
            return current_hash
        hashTree(root)
        # print(self.hashset)
        return list(self.res)

import collections

class Solution1(object):
    def findDuplicateSubtrees(self, root):
        trees = collections.defaultdict()
        trees.default_factory = trees.__len__
        count = collections.Counter()
        ans = []
        def lookup(node):
            if node:
                uid = trees[node.val, lookup(node.left), lookup(node.right)]
                count[uid] += 1
                if count[uid] == 2:
                    ans.append(node)
                return uid
        lookup(root)
        # print(trees)
        return ans

if __name__ == "__main__":
    t = stringToTreeNode("[94,93,95]")
    t = stringToTreeNode("[1,1,1,1,1,1,1,1,1,null,null,1,1,1]")
    prettyPrintTree(t)
    print(len(Solution().findDuplicateSubtrees(t)))