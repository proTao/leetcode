# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []:
            return None
        pivot = len(nums)//2
        r = TreeNode(nums[pivot])
        r.left = self.sortedArrayToBST(nums[:pivot])
        r.right = self.sortedArrayToBST(nums[pivot+1:])
        return r

def prettyPrintTree(node, prefix="", isLeft=True):
    if not node:
        print("Empty Tree")
        return

    if node.right:
        prettyPrintTree(node.right, prefix + ("│   " if isLeft else "    "), False)

    print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))

    if node.left:
        prettyPrintTree(node.left, prefix + ("    " if isLeft else "│   "), True)


s = Solution()
res = s.sortedArrayToBST([-10,-3,0,5,9])
prettyPrintTree(res)
