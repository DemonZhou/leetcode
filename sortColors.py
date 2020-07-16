class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        num0 = 0
        num2 = 0

        N = len(nums)
        for n in nums:
            if n == 0:
                num0 += 1
            elif n == 2:
                num2 += 1
        
        for i in range(N):
            if i >= 0 and i < num0:
                nums[i] = 0
            elif i < N and i >= N - num2:
                nums[i] = 2
            else:
                nums[i] = 1
    