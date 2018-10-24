from bisect import bisect_left
from collections import deque

class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        
        right = bisect_left(arr, x)
        left = right - 1
        count = 0
        res = deque([])
        length = len(arr)

        while count < k:
            if left < 0:
                res.extend(arr[right:right+k-count])
                break
            if right >= length:
                res.extendleft(arr[left:left-k+count:-1])
                break
            if abs(arr[left]-x) <= abs(arr[right]-x):
                res.appendleft(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1
            count += 1
        return list(res)
l = [0,1,2,2,2,3,6,8,8,9]
k = 5
x = 9
print(Solution().findClosestElements(l, k, x))