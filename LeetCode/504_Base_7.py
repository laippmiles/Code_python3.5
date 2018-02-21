#安慰智障的n进制转换
#“按n取余，结果倒置”
#42ms
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        FlagNa = 0
        if num == 0 :
            return '0'
        if num < 0:
            num = num * -1
            FlagNa = 1
        ans = []
        while num > 0:
            ans.append(str(num % 7))
            num = num // 7
        if FlagNa == 1:
            ans.append('-')
        ans = ''.join(ans)
        return ans[::-1]
#风骚的29ms版
#将7进制又看作“十进制”
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = 0
        count = 0
        posNeg = 0
        if num > 0:
            posNeg = 1
        num = abs(num)
        while(num != 0):
            rmd = num % 7
            res = num / 7
            result = result + rmd * (10**count)
            num = res
            count += 1
        if posNeg:
            return str(result)
        else:
            return str(-result)