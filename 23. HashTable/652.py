from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import defaultdict, Counter
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        index = defaultdict() # (root.val, leftidx, rightidx) -> rootidx
        index.default_factory = index.__len__
        counter = Counter()
        res = []
        def deeper(root):
            if root is None:
                return None
            leftidx = deeper(root.left)
            rightidx = deeper(root.right)
            rootidx = index[root.val, leftidx, rightidx]
            counter[rootidx] += 1
            if counter[rootidx] == 2:
                res.append(root)
            return rootidx
        deeper(root)
        return res

if __name__ == "__main__":
    pass