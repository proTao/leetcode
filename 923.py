from collections import Counter
from bisect import bisect_left as bisect

class Solution:
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        count = Counter(A)
        l = list(count.keys())
        l.sort()
        res = 0
        length = len(l)
        for i in range(length):
            if count[l[i]] > 2 and l[i] * 3 == target:
                res += count[l[i]] * (count[l[i]] - 1) * (count[l[i]]-2) // 6
            if count[l[i]] > 1:
                second_target = target-l[i]-l[i]
                if second_target in count and count[second_target]>=1 and second_target > l[i]:
                    res += count[l[i]]*(count[l[i]]-1)*count[second_target] // 2
                # third = bisect(l, third_target, i+1)
                # if third < length and l[third]==third_target:
                    # res += count[l[i]]*(count[l[i]]-1)*count[third_target] // 2
            second_target = (target - l[i])//2
            if second_target * 2 + l[i] == target and second_target in count and count[second_target]>1 and second_target > l[i]:
                res += count[l[i]] * count[second_target] * (count[second_target]-1) // 2
            for j in range(i+1, length):
                third_target = target-l[i]-l[j]
                if third_target > l[j] and third_target in count:
                    res += count[l[i]]*count[l[j]]*count[third_target]
                if third_target <= l[j]:
                    break
                # third = bisect(l, third_target, j+1)
                # if third < length and l[third]==third_target:
                #     res += count[l[i]]*count[l[j]]*count[third_target]
                # if third == length:
                #     break
        return res % 1000000007

A = [0,2,0]
target = 2
print(Solution().threeSumMulti(A, target))
