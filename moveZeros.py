class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        i = 0
        j = 0
        n = len(nums)
        
        while i < n:
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            i += 1
        
        for x in range(j,n):
            nums[x] = 0