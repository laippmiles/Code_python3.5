#一如既往慢出翔的初版
#55ms
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        else:
            for i in range(0,2):
                del nums[nums.index(max(nums))]
            return max(nums)

#不懂我刚刚写错哪了- -
#别家的
#原来可以用集合做啊
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        if len(nums)<3:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)