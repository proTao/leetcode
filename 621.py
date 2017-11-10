class Solution(object):
    dic={}
    schedule = []
    def getBigger(self, a, b):
        return self.dic[a]>self.dic[b] and a or b

    def insertTask(self, index, task):
        while(True):

            if index>len(self.schedule)-1:
                self.schedule.extend([-1]*(index-len(self.schedule)+1))


            if self.schedule[index] == -1:
                self.schedule[index] = task
                return index
            else:
                index += 1


                

        
        

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        
        for task in tasks:
            if task in self.dic:
                self.dic[task] = self.dic[task] + 1
            else:
                self.dic.setdefault(task, 1)

        top_task = reduce(self.getBigger, self.dic)
        top_task_num = self.dic[top_task]
        self.schedule = [-1] * ((n+1)*(top_task_num-1)+1)
        print(self.dic)
        while(self.dic):
            top_task = reduce(self.getBigger, self.dic)
            top_task_num = self.dic.pop(top_task)
            if -1 in self.schedule:
                idle = self.schedule.index(-1)
            else:
                idle = len(self.schedule)

            #insert task to the self.schedule
            while top_task_num > 0:
                idle = self.insertTask(idle, top_task) + n + 1
                top_task_num -= 1
            print(self.schedule)
        return len(self.schedule)

s=Solution()

s.leastInterval(['A','A','A','A','B','B','B','C','C','C'],1)
