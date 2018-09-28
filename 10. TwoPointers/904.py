from collections import deque
class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        # 向左走向右走一样的
        if len(tree) <= 2:
            return len(tree)
        dp = {}
        last_two = deque([tree[0], tree[1]])
        for i in tree:
            if i not in dp:
                dp[i] = 0
        dp[tree[0]] += 1
        dp[tree[1]] += 1
        if tree[0] == tree[1]:
            onlyone = True
            continous_len = 2
        else:
            onlyone = False
            continous_len = 1
        res = sum(dp.values())
        for i, n in enumerate(tree[2:], start=2):
            if onlyone:
                dp[n] += 1
                if n != last_two[1]:
                    onlyone = False
                    continous_len = 1
                else:
                    continous_len += 1
                last_two.popleft()
                last_two.append(n)
            elif n in last_two:
                dp[n] += 1
                if n == last_two[0]:
                    last_two[0], last_two[1] = last_two[1], last_two[0]
                    continous_len = 1
                else:
                    continous_len += 1
            else:
                # 要替换
                dp[last_two[0]] = 0
                dp[n] += 1
                last_two.popleft()
                last_two.append(n)
                dp[last_two[0]] = continous_len
                continous_len = 1
            if onlyone:
                res += 1
            else:
                res = max(res, dp[last_two[0]]+dp[last_two[1]])
        return res
        
a = [3,3,3,1,2,1,1,2,3,3,4] # 5
# a = [1,0,1,4,1,4,1,2,3] # 5
a = [1,2,3,2,2] # 4
print(Solution().totalFruit(a))
                

