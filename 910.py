class Solution(object):
    def smallestRangeII(self, A, k):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        dp = {}
        dp["add"] = []
        dp["minus"] = []
        dp["add"].append((A[0] + k, A[0] + k))
        dp["minus"].append((A[0] - k, A[0] - k))
        gap = 0

        for a in A[1:]:
            # "minus"
            temp = a - k
            if dp["minus"][-1][0] <= temp <= dp["minus"][-1][1] or\
                dp["add"][-1][0] <= temp <= dp["add"][-1][1]:
                if dp["minus"][-1][1] - dp["minus"][-1][0] <\
                    dp["add"][-1][1] - dp["add"][-1][0]:
                    new_minus = dp["minus"][-1]
                else:
                    new_minus = dp["add"][-1]
            elif temp > dp["add"][-1][0] and temp > dp["minus"][-1][0]:
                if dp["add"][-1][1] > dp["minus"][-1][1]:
                    new_minus = (dp["add"][-1][0], temp)
                else:
                    new_minus = (dp["minus"][-1][0], temp)
            elif temp < dp["add"][-1][0] and temp < dp["minus"][-1][0]:
                if dp["add"][-1][0] < dp["minus"][-1][0]:
                    new_minus = (temp, dp["add"][-1][1])
                else:
                    new_minus = (temp, dp["minus"][-1][1])
            elif dp["add"][-1][1] < temp < dp["minus"][-1][0]:
                if temp - dp["add"][-1][1] < dp["minus"][-1][0] - temp:
                    new_minus = (dp["add"][-1][0], temp)
                else:
                    new_minus = (temp, dp["minus"][-1][1])
            else:
                if temp - dp["minus"][-1][1] <= dp["add"][-1][0] - temp:
                    new_minus = (dp["minus"][-1][0], temp)
                else:
                    new_minus = (temp, dp["add"][-1][1])

            # add
            temp = a + k
            if dp["minus"][-1][0] <= temp <= dp["minus"][-1][1] or\
                dp["add"][-1][0] <= temp <= dp["add"][-1][1]:
                if dp["minus"][-1][1] - dp["minus"][-1][0] <\
                    dp["add"][-1][1] - dp["add"][-1][0]:
                    new_plus = dp["minus"][-1]
                else:
                    new_plus = dp["add"][-1]
            elif temp > dp["add"][-1][0] and temp > dp["minus"][-1][0]:
                if dp["add"][-1][1] > dp["minus"][-1][1]:
                    new_plus = (dp["add"][-1][0], temp)
                else:
                    new_plus = (dp["minus"][-1][0], temp)
            elif temp < dp["add"][-1][0] and temp < dp["minus"][-1][0]:
                if dp["add"][-1][0] < dp["minus"][-1][0]:
                    new_plus = (temp, dp["add"][-1][1])
                else:
                    new_plus = (temp, dp["minus"][-1][1])
            elif dp["add"][-1][1] < temp < dp["minus"][-1][0]:
                if temp - dp["add"][-1][1] < dp["minus"][-1][0] - temp:
                    new_plus = (dp["add"][-1][0], temp)
                else:
                    new_plus = (temp, dp["minus"][-1][1])
            else:
                if temp - dp["minus"][-1][1] <= dp["add"][-1][0] - temp:
                    new_plus = (dp["minus"][-1][0], temp)
                else:
                    new_plus = (temp, dp["add"][-1][1])

            gap = min(new_minus[1]-new_minus[0], new_plus[1]-new_plus[0])
            dp["minus"].append(new_minus)
            dp["add"].append(new_plus)
        print(dp["add"])
        print(dp["minus"])
        return gap

a = [9,10,0,7]
k = 1
print(Solution().smallestRangeII(a, k))