class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        temp = root
        while temp.left:
            temp = temp.left
        self.last_node = temp
        self.error_node = None
        self.error_last_node = None
        def inorder(root):
            # return value is a booean value and means the tree has been recovered
            flag = root.left and inorder(root.left) or False

            if flag is False:
                if root.val < self.last_node.val:
                    if self.error_node is None:
                        self.error_node = root
                        self.error_last_node = self.last_node
                        self.last_node = root
                    else:
                        self.error_last_node.val, root.val = root.val, self.error_last_node.val
                        flag = True
                else:
                    self.last_node = root
            
            return flag or root.right and inorder(root.right) or False

        # print(self.last_node.val)
        if inorder(root) is False:
            self.error_node.val, self.error_last_node.val = self.error_last_node.val, self.error_node.val
