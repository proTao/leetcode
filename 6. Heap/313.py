from heapq import heappop, heappush
import heapq
class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        heap = [1]
        marked = set()
        while n > 0:
            res = heappop(heap)
            for x in filter(lambda x:x not in marked, map(lambda x:res*x, primes)):
                # print(res, "->", x)
                heappush(heap, x)
                marked.add(x)
            n -= 1
        print(len(heap))
        return res

class Solution1:
    def nthSuperUglyNumber(self, n, primes):
        uglies = [1]
        def gen(prime):
            for ugly in uglies:
                yield ugly * prime
        merged = heapq.merge(*map(gen, primes))
        while len(uglies) < n:
            ugly = next(merged)
            # print(uglies)
            if ugly != uglies[-1]:
                uglies.append(ugly)
        return uglies[-1]


import cProfile, pstats
n=10000
primes=[2,3,5,13,19,29,31,41,43,53,59,73,83,89,97,103,107,109,127,137,139,149,163,173,179,193,197,199,211,223,227,229,239,241,251,257,263,269,271,281,317,331,337,347,353,359,367,373,379,389,397,409,419,421,433,449,457,461,463,479,487,509,521,523,541,547,563,569,577,593,599,601,613,619,631,641,659,673,683,701,709,719,733,739,743,757,761,769,773,809,811,829,857,859,881,919,947,953,967,971]
# cProfile.run("Solution().nthSuperUglyNumber(n, primes)","timeit")
cProfile.run("Solution1().nthSuperUglyNumber(n, primes)","timeit")
p = pstats.Stats('timeit')
p.sort_stats('time')
p.print_stats()
