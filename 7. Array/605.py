# define DFA status
STATUS_EXIST_FLOWER = 1
STATUS_LEFT_EMPTY = 2 
STATUS_MIDDLE_POSITION = 3
STATUS_STOP_OR_CONTINUE = 4

class Solution(object):
    def DFAchangeStatus(self, current_status, next_position):
        if next_position == 1:
            return STATUS_EXIST_FLOWER
        else:
            if current_status == STATUS_EXIST_FLOWER:
                return STATUS_LEFT_EMPTY
            if current_status == STATUS_LEFT_EMPTY:
                return STATUS_MIDDLE_POSITION
            if current_status == STATUS_MIDDLE_POSITION:
                return STATUS_STOP_OR_CONTINUE
            if current_status == STATUS_STOP_OR_CONTINUE:
                return STATUS_MIDDLE_POSITION

    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        position = 0

        
        # start position is same as there is an empty on the left
        status = STATUS_LEFT_EMPTY

        for i in flowerbed:
            status = self.DFAchangeStatus(status, i)
            # print("->"+str(status))
            if status == STATUS_STOP_OR_CONTINUE:
                position += 1

        # start position is same as there is an empty on the left
        if status == STATUS_MIDDLE_POSITION:
            position += 1

        # print(position)
        if position >= n:
            return True
        else:
            return False

s = Solution()

print(s.canPlaceFlowers([1,0,0,0,0,1,0],2))
print(s.canPlaceFlowers([0,0,1,0,1],1))
print(s.canPlaceFlowers([1,0,1,0,0],1))