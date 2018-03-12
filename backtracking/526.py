
DEBUG = False
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """

        # initial
        
        self.visited = [0 for i in range(N+1)]
        self.path = []
        self.swappable_list = [[],]
        for i in range(1,N+1):
            self.swappable_list.append(self.findSwappable(i,N))

        if DEBUG:
            for i,l in enumerate(self.swappable_list):
                print(i,l)


        res = self.search()
        return res
            


    def findReducible(self, x):
        if x == 1:
            return [1]
        res = []
        square_root_x = int(x**0.5//1)
        # print(square_root_x)
        i = 1
        while i <= square_root_x:
            if x%i == 0:
                res.append(i)
                if i ** 2 != x:
                    # print(i)
                    res.append(int(x/i))
            i += 1

        return res

    def findTimerLessThanN(self, x, N):
        # not include x self
        i = N // x
        res = []
        while i > 1:
            res.append(x*i)
            i -= 1
        return res

    def findSwappable(self, x, N):
        res = self.findReducible(x)
        res.extend(self.findTimerLessThanN(x, N))
        return res

    def search(self, start=0, now=0):
        if DEBUG:
            print("search", start, now)
            print(self.path)
        if start == 0:
            for i in range(1,len(self.visited)):
                if self.visited[i]==0:
                    start = i
                    now = i
                    if DEBUG:
                        print("find a new start", start)
                    break
            else:
                if DEBUG:
                    print("-----------------find a solution!!!!!!!!!------------")
                return 1

        res = 0
        for swap_to in self.swappable_list[now]:
            if self.visited[swap_to] == 0:
                self.visited[swap_to] = 1
                self.path.append(swap_to)
                if DEBUG:
                    if(now > 0):
                        print("from",now,"swap_to", swap_to)
                if swap_to == start:
                    res += self.search()
                else:
                    res += self.search(start, swap_to)
                self.visited[swap_to] = 0
                self.path.pop()
        return res



s = Solution()


""" faster implement
cache = {}
class Solution(object):
    def countArrangement(self, N):
        def helper(i, X):
            if i == 1:
                return 1
            key = (i, X)
            if key in cache:
                return cache[key]
            total = 0
            for j in range(len(X)):
                if X[j] % i == 0 or i % X[j] == 0:
                    total += helper(i - 1, X[:j] + X[j + 1:])
            cache[key] = total
            return total
        return helper(N, tuple(range(1, N + 1)))

s = Solution()
print(s.countArrangement(15))
"""


# print(s.findReducible(9))


res = s.countArrangement(17)
print(res)
