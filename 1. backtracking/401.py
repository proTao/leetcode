class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        def deeper(time, rest_light):
            # print(time, rest_light)
            if rest_light == 0:
                time+="0"*(10-len(time))
                minute = int(time[4:],2)
                time_str = str(int(time[:4],2))+":"+("0" if minute <10 else "")+str(minute)
                res.append(time_str)
                return

            # pruning
            if 10 - len(time)-2 == rest_light and len(time) == 1:
                print("pruning",time,rest_light)
                time += "011110111"
                minute = int(time[4:],2)
                time_str = str(int(time[:4],2))+":"+("0" if minute <10 else "")+str(minute)
                res.append(time_str)
                return
            if 10 - len(time)-1 == rest_light and len(time) >= 2 and len(time) <= 6:
                print("pruning",time,rest_light)
                time += "1"*(6-len(time))+"0111"
                minute = int(time[4:],2)
                time_str = str(int(time[:4],2))+":"+("0" if minute <10 else "")+str(minute)
                res.append(time_str)
                return

            # if 10 - len(time) == rest_light and len(time) >= 7:
            #     print("pruning",time,rest_light)
            #     time += "1"*(10-len(time))
            #     minute = int(time[4:],2)
            #     time_str = str(int(time[:4],2))+":"+("0" if minute <10 else "")+str(minute)
            #     res.append(time_str)
            #     return


            # the next position is light
            if len(time)<10:
                deeper(time+"0",rest_light)

                # the next position is light
                if not (len(time)==1 and time[0]=="1") and \
                    not (len(time)==7 and time[4:7] == "111"):
                    deeper(time+"1", rest_light-1)

            

        deeper("", num)
        return res


s = Solution()
res = s.readBinaryWatch(8)
print(res)