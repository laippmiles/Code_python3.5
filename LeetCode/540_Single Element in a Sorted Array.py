#39ma
#基本就是各个数据结构切换切换切
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = set(nums[0::2])
        b = set(nums[1::2])
        c = list(set(nums) - (a&b))
        return c[0]
#42ms
#因为要走一趟循环，反而会稍慢一点
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in range(0,len(nums)):
            a = a ^ nums[i]
        return a

#别人家的29ms
#和自己最初的想法反而很接近
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        while (index + 1) < len(nums):
            if nums[index] != nums[index+1]:
                return nums[index]
            index += 2
        return nums[-1]