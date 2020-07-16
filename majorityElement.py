class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return nums[1]
        nums.sort()

        return nums[len(nums) // 2 + 1]