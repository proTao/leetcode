from collections import defaultdict
class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # initial
        res = []
        studied = [False for _ in range(numCourses)]
        pre_count = [0 for _ in range(numCourses)]
        connect = defaultdict(lambda: [])
        for course, precourse in prerequisites:
            pre_count[course] += 1
            connect[precourse].append(course)


        for _ in range(numCourses):
            # print(pre_count)
            # print(connect)
            for i in range(numCourses):
                if pre_count[i] == 0 and not studied[i]:
                    # print("choose",i)
                    res.append(i)
                    studied[i] = True
                    for j in connect[i]:
                        pre_count[j] -= 1
                    break
            else:
                return []

        return res

    def findOrder(self, numCourses, prerequisites):
        # 上边的方法速度慢是因为每次找下一个能选择的课程需要遍历，通常这种遍历都很费时间，naive的方法是用空间换时间
        # 比如studied本来是用一个list存已经选过的课程，这样本次判断是否已经选过需要遍历list
        # 改为标志位的方法速度得以提升
        res = []
        studied = [False for _ in range(numCourses)]
        pre_count = [0 for _ in range(numCourses)]
        connect = defaultdict(lambda: [])
        stack = []
        for course, precourse in prerequisites:
            pre_count[course] += 1
            connect[precourse].append(course)

        for i in range(numCourses):
            if pre_count[i] == 0:
                stack.append(i)

        while stack:
            choose_course = stack.pop()
            res.append(choose_course)
            if not connect[choose_course]:
                continue
            for next_course in connect[choose_course]:
                pre_count[next_course] -= 1
                if pre_count[next_course] == 0:
                    stack.append(next_course)

        return [] if len(res)<numCourses else res

s = Solution()
res = s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
print(res)
