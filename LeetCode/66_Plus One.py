#42ms
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = digits[::-1]
        sum = 0
        for i in range(0,len(digits)):
            sum += digits[i]*(10**i)
        sum = str(sum+1)
        ans = []
        for w in sum:
            ans.append(int(w))
        return ans
#28ms
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        for i in range(len(digits)):
            if digits[i] + 1 != 10:
                digits[i] = digits[i] + 1
                break
            else:
                digits[i] = 0
                if i == len(digits) - 1:
                    digits.append(1)
        digits.reverse()
        return digits