class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math
        for i in range(int(math.sqrt(area)),0,-1):
            if area % i == 0:
                return [area/i,i]
