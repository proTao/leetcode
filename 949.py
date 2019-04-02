from collections import Counter
class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        self.d1 = None
        self.d2 = None
        self.d3 = None
        self.d4 = None
        try:
            for d1 in sorted(filter(lambda x:0<=x<=2, A), reverse=True):
                index = A.index(d1)
                A[index] = -1;
                self.secondStep(d1, A);
                if self.d4 is not None:
                    return "{}{}:{}{}".format(d1, self.d2, self.d3, self.d4)
                A[index] = d1;
            return ""
        except ValueError:
            return ""

    def secondStep(self, d1, A):
        if d1 == 2:
            try:
                for d2 in sorted(filter(lambda x:0<=x<=3, A), reverse=True):
                    index = A.index(d2)
                    A[index] = -1;
                    self.thirdStep(d2, A);
                    if self.d4 is not None:
                        self.d2 = d2
                        return 
                    A[index] = d2;
                self.d2 = None
                return
            except ValueError as e:
                self.d2 = None
                return ""
        else:
            for d2 in sorted(filter(lambda x:0<=x<=9, A), reverse=True):
                index = A.index(d2)
                A[index] = -1;
                self.thirdStep(d2, A);
                if self.d4 is not None:
                    self.d2 = d2
                    return                
                A[index] = d2;
            return

    def thirdStep(self, d2, A):
        try:
            for d3 in sorted(filter(lambda x:0<=x<=5, A), reverse=True):
                index = A.index(d3)
                A[index] = -1;
                self.lastStep(d3, A);
                if self.d4 is not None:
                    self.d3 = d3
                    return
                A[index] = d3;
            self.d3 = None
            return
        except ValueError:
            self.d3 = None
            return 
    
    def lastStep(self, d3, A):
        try:
            for d4 in sorted(filter(lambda x:0<=x<=9, A), reverse=True):
                self.d4 = d4;
        except ValueError:
            return ""


        


if __name__ == "__main__":
    print(Solution().largestTimeFromDigits([4,4,5,5]))





        
        