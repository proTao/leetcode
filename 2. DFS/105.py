from treetools import TreeNode, prettyPrintTree

class Solution:
    def buildTree2(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        root_inorder_index = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:1+root_inorder_index],\
                                    inorder[:root_inorder_index])
        root.right = self.buildTree(preorder[1+root_inorder_index:],\
                                    inorder[root_inorder_index+1:])
        return root

    def buildTree(self, preorder, inorder):
        inorder_dict = {val:index for index,val in enumerate(inorder)}

        def buildTreeCore(pre_l, pre_r, in_l, in_r):
            if pre_l == pre_r:
                return None

            root = TreeNode(preorder[pre_l])
            root_inorder_index = inorder_dict[root.val]
            root.left = buildTreeCore(pre_l+1,pre_l+1+root_inorder_index-in_l,\
                                    in_l,root_inorder_index)
            root.right = buildTreeCore(pre_l+1+root_inorder_index-in_l, pre_r,\
                                    root_inorder_index+1,in_r)
            return root

        return buildTreeCore(0, len(preorder), 0, len(preorder))

s = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
t = s.buildTree(preorder, inorder)
prettyPrintTree(t)