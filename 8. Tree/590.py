
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []

        self.res = []
        def deeper(root):
            for i in root.children:
                deeper(i)
            self.res.append(root.val)
        
        deeper(root)
        return self.res
