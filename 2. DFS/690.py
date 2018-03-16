"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, target_id):
        """
        :type employees: list[Employee]
        :type id: int
        :rtype: int

        input is:[<__main__.Employee object at 0x7f8f2d8b24a8>,
                  <__main__.Employee object at 0x7f8f2d8b2518>,
                  ...]
        """

        # method1 : by reduce type dfs
        self.dict = {}
        for e in employees:
            self.dict[e.id] = e


        def dfs(target_id):
            e = self.dict[target_id]
            return e.importance + sum([dfs(sub_id) for sub_id in e.subordinates])
        return dfs(target_id)


class Solution:
    def getImportance(self, employees, target_id):
        # method2 : by backtrack type dfs
        self.dict = {}
        for e in employees:
            self.dict[e.id] = e
        
        self.res = 0
        def deeper(target_id):
            self.res += self.dict[target_id].importance
            for next_id in self.dict[target_id].subordinates:
                deeper(next_id)

        deeper(target_id)
        return self.res





s = Solution()


        