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



s = Solution()
res = s.sortedArrayToBST([-10,-3,0,5,9])
