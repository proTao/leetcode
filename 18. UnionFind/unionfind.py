class UnionFind():
    def __init__(self, length):
        self.length = length
        self.components = length
        self.pre = [i for i in range(length)]

    def root(self, i):
        # find root
        length = 0
        c = i
        while self.pre[i] != i:
            i = self.pre[i]
            length += 1
        root = i

        # path compress
        temp = self.pre[c]
        while temp != c:
            self.pre[c] = root
            c = temp
            temp = self.pre[c]
        return root

    def check(self, i, j):
        return self.root(i) == self.root(j)

    def add(self, i, j):
        root_i, root_j = self.root(i), self.root(j)
        if root_i != root_j:
            self.pre[root_i] = root_j
            self.components -= 1

    def componentsNum(self):
        return self.components

    def show(self):
        print(self.length, self.components)
        print(self.pre)

class DynamicUnionFind(UnionFind):
    def __init__(self, length=1):
        UnionFind.__init__(self, length)

    def add(self, i, j):
        if i >= self.length or j >= self.length:
            new_length = max(i,j) + 1
            self.components += new_length - self.length
            self.length = new_length
            self.pre += [i for i in range(len(self.pre), new_length)]

        root_i, root_j = self.root(i), self.root(j)
        if root_i != root_j:
            self.pre[root_i] = root_j
            self.components -= 1

'''
def DynamicUnionFind(length=1):
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
'''

if __name__ == "__main__":
    uf = DynamicUnionFind()
    uf.add(9,10)
    uf.show()
    uf.add(8,9)
    uf.show()
    uf.add(10,1)
    uf.show()
    uf.add(8,2)
    uf.show()
