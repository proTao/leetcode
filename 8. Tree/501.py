from treetools import *
class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        max_count = 1
        it = inorder(root)
        res = [next(it)]
        last = res[0]
        count = 1
        for i in it:
            if i == last:
                count = count + 1
            else:
                last = i
                count = 1
            if count == max_count:
                    res.append(i)
            elif count > max_count:
                res = [i]
                max_count = count
        return res

def inorder(root):
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        yield curr.val
        curr = curr.right


t = stringToTreeNode("[]")
prettyPrintTree(t)
print(Solution().findMode(t))
