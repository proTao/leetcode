def UnionFind(length=1):
    components = length
    pre = [i for i in range(length)]
    def __root(i):
        # find root
        length = 0
        c = i
        while pre[i] != i:
            i = pre[i]
            length += 1
        root = i

        # path compress
        temp = pre[c]
        while temp != c:
            pre[c] = root
            c = temp
            temp = pre[c]
        return root

    def __check(i, j):
        return __root(i) == __root(j)

    def __add(i, j):
        nonlocal pre
        nonlocal components
        # expand pre
        if i >= length or j >= length:
            # raise FutureWarning("length overflow and auto expand")
            new_length = max(i,j) + 1
            components += new_length - len(pre)
            pre += [i for i in range(len(pre), new_length)]

        # add
        root_i, root_j = __root(i), __root(j)
        if root_i != root_j:
            pre[root_i] = root_j
            components -= 1
            return True
        else:
            return False

    def __count():
        return components

    def f():
        # return function object
        pass
    f.root = __root
    f.check = __check
    f.add = __add
    f.count = __count
    return f

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        uf = UnionFind()
        for i, j in edges:
            flag = uf.add(i,j)
            if flag == False:
                return [i,j]

edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
print(Solution().findRedundantConnection(edges))