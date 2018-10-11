DEBUG = True
cache = {}
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        res = []

        if n == 0 or k == 0 or k > n:
            return res

        def deeper(path = []):
            if len(path) == k:
                res.append(path)

            if len(path) == 0:
                start = 1
            else:
                start = path[-1] + 1
            for i in range(start, n+1):
                deeper(path + [i])

            return 

        deeper()
        return res


    def combine2(self, n, k):
        
        if k == 1 :
            return [[i] for i in range(1,n+1)]
        if k == n :
            return [list(range(1,n+1))]

        else:
            return [i + [n] for i in self.combine2(n-1,k-1)] + self.combine2(n-1,k)

    
    def combine3(self, n, k):
        if k == 1 :
            return [[i] for i in range(1,n+1)]
        if k == n :
            return [list(range(1,n+1))]
        if (n,k) in cache:
            # print("hit")
            return cache[(n,k)]

        else:
            res = [i + [n] for i in self.combine3(n-1,k-1)] + self.combine3(n-1,k)
            if (n,k) not in cache:
                # print((n,k),"put into cache")
                cache[(n,k)] = res
            return res

s = Solution()
print(len(s.combine3(21,10)))