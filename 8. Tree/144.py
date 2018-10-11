def preOrderTraversal(root):
    if root is None:
        raise StopIteration
    stack = [root]
    while stack:
        curr = stack.pop()
        yield curr.val

        curr.right and stack.append(curr.right)
        curr.left and stack.append(curr.left)


class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return list(preOrderTraversal(root))