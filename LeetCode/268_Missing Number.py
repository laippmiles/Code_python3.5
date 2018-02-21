#和single number一样用异或的解法（59ms）
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(range(0, len(nums) + 1)) + nums
        a = 0
        for b in nums:
            a = a ^ b
        return a
# 走数学公式的35ms版
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(nums)*(len(nums)+1)/2 - sum(nums)

