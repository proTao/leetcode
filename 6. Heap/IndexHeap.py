class MinHeap:
    def __init__(self):
        self.N = 0
        self.pq = [None]

    def isEmpty(self):
        return self.N == 0

    def size(size):
        return self.N

    def insert(self, key):
        print("IndexMinHeap Insert", index)
        self.N += 1
        self.pq.append(key)
        self._swim(self.N)

    def delMin(self):
        self._exch(1, self.N)
        self.N -= 1
        res = self.pq.pop()
        self._sink(1)
        return res

    def _comp(self, i, j):
        return self.pq[i] > self.pq[j]

    def _exch(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

    def _swim(self, k):
        while k > 1 and self._comp(k>>1, k):
            self._exch(k>>1 , k)
            k = k>>1

    def _sink(self, k):
        while k << 1 <= self.N:
            j = k << 1
            if j < self.N and self._comp(j, j+1):
                j += 1
            if not self._comp(k, j):
                break
            self._exch(k, j)
            k = j

    def __str__(self):
        return str(self.pq[1:])

class IndexMinHeap(MinHeap):
    def __init__(self):
        self.keys = {}
        self.qp = {}
        MinHeap.__init__(self)


    def contains(self, index):
        return index in qp

    def insert(self, index, key):
        print("IndexMinHeap Insert", index, "with weight", key)
        self.N += 1
        self.qp[index] = self.N
        self.pq.append(index)
        self.keys[index] = key
        self._swim(self.N)

    def delMin(self):
        self._exch(1, self.N)
        indexOfMin = self.pq.pop()
        self.N -= 1
        self._sink(1)
        del self.keys[indexOfMin]
        del self.qp[indexOfMin]
        return indexOfMin

    def change(self, index, key):
        self.keys[index] = key
        self._swim(self.qp[index])
        self._sink(self.qp[index])


    def keyOf(self, index):
        return self.keys[index]

    def delete(self, index):
        i = self.qp[index];
        self.n -= 1
        self._exch(i, self.n);
        self._swim(i);
        self._sink(i);
        self.keys[index] = null;
        self.qp[index] = -1;

    def show(self):
        print("最近节点", a.minIndex())
        print("最近距离", a.minWeight())
        print([(i, self.keys[i]) for i in self.pq[1:]])
        print("pq", self.pq)
        print("qp", self.qp)


    def _comp(self, i, j):
        return self.keys[self.pq[i]] > self.keys[self.pq[j]]

    def _exch(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j;



    def minWeight(self):
        return self.keys[self.pq[1]]

    def minIndex(self):
        return self.pq[1]

if __name__ == "__main__":
    a = IndexMinHeap()
    a.insert('a', 5)
    a.insert('b', 3)
    a.insert('c', 6)
    a.insert('d', 2)
    a.show()
    print(a.keyOf('a'))


    a.change('a', 1)
    a.show()
    print(a.keyOf('a'))