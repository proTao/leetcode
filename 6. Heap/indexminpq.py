class IndexMinPQ:
    def __init__(self, N):
        self.maxN = N;        # maximum number of elements on PQ
        self.n = 0;           # number of elements on PQ
        self.pq = []        # binary heap using 1-based indexing
        self.qp = []       # inverse of pq - qp[pq[i]] = pq[qp[i]] = i
        self.keys = []     # keys[i] = priority of i


    def IndexMinPQ(maxN):
        this.maxN = maxN;
        n = 0;
        keys = (Key[]) new Comparable[maxN + 1];    # make this of length maxN??
        pq   = new maxN + 1];
        qp   = new maxN + 1];                   # make this of length maxN??
        for (i = 0; i <= maxN; i++)
            qp[i] = -1;
    


    def isEmpty() 
        return n == 0;
    


    def contains(i) 
        if (i < 0 || i >= maxN) throw new IndexOutOfBoundsException();
        return qp[i] != -1;
    


    def size() 
        return n;
    


    def insert(i,key) 
        n++;
        qp[i] = n;
        pq[n] = i;
        keys[i] = key;
        swim(n);

    def minIndex() 
        return pq[1];
    


    def minKey() 
        return keys[pq[1]];
    


    def delMin() 
        min = pq[1];
        exch(1, n--);
        sink(1);
        assert min == pq[n+1];
        qp[min] = -1;        # delete
        keys[min] = null;    # to help with garbage collection
        pq[n+1] = -1;        # not needed
        return min;
    
    def keyOf(i) 
        else return keys[i];
    

    def changeKey(i,key) 
        keys[i] = key;
        swim(qp[i]);
        sink(qp[i]);
    

    def change(i,key) 
        changeKey(i, key);
    


    def decreaseKey(i,key) 
        keys[i] = key;
        swim(qp[i]);
    

    def increaseKey(i,key) 
        keys[i] = key;
        sink(qp[i]);
    


    def  delete(i) 
        index = qp[i];
        exch(index, n--);
        swim(index);
        sink(index);
        keys[i] = null;
        qp[i] = -1;
    

    def greater(i, j)
        return keys[pq[i]] > keys[pq[j]]
    

    def exch(i, j):
        swap = self.pq[i];
        pq[i] = self.pq[j];
        pq[j] = self.swap;
        self.qp[pq[i]] = i;
        self.qp[pq[j]] = j;
    

    def swim(k):
        while k > 1 and self.greater(k//2, k):
            self.exch(k, k//2);
            k = k//2
        
    

    def sink(k):
        while 2*k <= n:
            j = 2*k;
            if (j < n and self.greater(j, j+1)):
                j+=1
            if not self.greater(k, j):
                break
            self.exch(k, j)
            k = j
        
    



    def Iterator<ger> iterator()  return new HeapIterator(); 

    class HeapIterator implements Iterator<ger> 
        # create a new pq
        IndexMinPQ<Key> copy;

        # add all elements to copy of heap
        # takes linear time since already in heap order so no keys move
        def HeapIterator() 
            copy = new IndexMinPQ<Key>(pq.length - 1);
            for (i = 1; i <= n; i++)
                copy.insert(pq[i], keys[pq[i]]);
        

        def boolean hasNext()   return !copy.isEmpty();                     
        def  remove()       throw new UnsupportedOperationException();  

        def ger next() 
            if (!hasNext()) throw new NoSuchElementException();
            return copy.delMin();
        
    
    