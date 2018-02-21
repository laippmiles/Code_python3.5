#42ms
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[0] >= target:
            return 0
        if nums[-1] <target:
            return len(nums)
        higher = 1
        for i in range(0,len(nums)):
            if target == nums[i]:
                return i
            if target < nums[i] :
                higher = 0
            if higher == 0:
                return i
#28ms
#二分查找法
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if  target < nums[mid] :
                end = mid - 1
            elif  target > nums[mid] :
                start = mid + 1
            else:
                return mid
        if mid > end:
            return mid
        if start > mid:
            return start