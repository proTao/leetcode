from treetools import TreeNode, stringToTreeNode, prettyPrintTree

def InOrderTraversal(root:TreeNode, returnval=True):
    if root is None:
        raise StopIteration
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        if returnval:
            yield curr.val
        else:
            yield curr
        curr = curr.right

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return list(InOrderTraversal(root))

a = stringToTreeNode("[1,null,2,3]")
prettyPrintTree(a)
print(Solution().inorderTraversal(a))