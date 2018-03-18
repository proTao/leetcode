from treetools import TreeNode
import treetools as tt

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        inorder_index_dict = {val:index for index,val in enumerate(inorder)}
        def buildTreeCore(in_l, in_r, post_l, post_r):
            if in_r == in_l:
                return None

            root_inorder_index = inorder_index_dict[postorder[post_r - 1]]
            root = TreeNode(postorder[post_r - 1])
            
            root.left = buildTreeCore(in_l,root_inorder_index,\
                    post_l, post_l+root_inorder_index-in_l)
            root.right = buildTreeCore(root_inorder_index+1, in_r,\
                    post_l+root_inorder_index-in_l, post_r-1)

            return root

        return buildTreeCore(0, len(inorder), 0, len(postorder))

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
t = Solution().buildTree(inorder, postorder)
tt.prettyPrintTree(t)
