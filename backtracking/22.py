class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = []
        def deeper(path, l, r):
            print(path, l, r)
            # l: how many ( have not used
            if l == 0 and r == 0:
                res.append(path)
                return 

            # pruning
            if l == 0:
                res.append(path+")"*r)
                return

            if r > l :
                deeper(path+")", l, r-1)
            
            # (
            if l > 0:
                deeper(path+"(", l-1, r)


        deeper("",n,n)
        return res

    def generateParenthesis2(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = []
        cache = {}
        def deeper(path, l, r):
            # print(path, l, r)
            if l == 0 and r == 0:
                res.append(path)
                # print("-----------got one solution",path,"-------")
                return 

            if l == r and l in cache:
                temp = [path+i for i in cache[l]]
                # print("read from cache", l, cache[l],"and exend to result",temp)
                res.extend(temp)
                return 

            # )
            if r > l :
                deeper(path+")", l, r-1)
                if r - 1 == l and l > 0 and l not in cache:
                    cache[l] = [i[-2*l:] for i in res]
                    # print("put into cache", l, cache[l])
            # (
            if l > 0:
                deeper(path+"(", l-1, r)


        deeper("",n,n)
        return res

        

s = Solution()
res = s.generateParenthesis(5)
print("res",len(res))