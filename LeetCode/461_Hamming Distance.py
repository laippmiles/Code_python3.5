#这个用移位逻辑写会快很多
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xx = bin(x).replace('0b','')
        yy = bin(y).replace('0b','')
        if x>y:
            yy ='0'*abs(len(xx)-len(yy)) + yy
        else:
            xx = '0' * abs(len(xx) - len(yy)) + xx
        rtype = 0
        for i in range(0,len(xx)):
            if xx[i] != yy[i]:
                rtype +=1
        return rtype