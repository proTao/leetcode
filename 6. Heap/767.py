from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        counter = [[-i[1], i[0]] for i in Counter(S).items()]
        heapq.heapify(counter)
        res = []
        self.useItem(res, counter, heapq.heappop(counter))

        while counter:
            most_freq = heapq.heappop(counter)
            if most_freq[1] == res[-1]:
                if counter:
                    self.useItem(res, counter, heapq.heappop(counter))
                    heapq.heappush(counter, most_freq)
                else:
                    return ""
            else:
                self.useItem(res, counter, most_freq)
        return "".join(res)

    
    def useItem(self, res, c, item):
        print(c,item)
        res.append(item[1])
        item[0] += 1 
        if item[0] < 0:
            heapq.heappush(c, item)




print(Solution().reorganizeString("aaab"))
