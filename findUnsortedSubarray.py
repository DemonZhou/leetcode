class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left , right = 1000, 0

        stack = []

        N = len(nums)

        for i in range(N):
            while len(stack) > 0 and nums[stack[-1]] > nums[i]:
                left = min(left, stack.pop())
            stack.append(i)
        
        stack = []

        for i in range(N -1 , -1, -1):
            while len(stack) > 0 and nums[stack[-1]] < nums[i]:
                right = max(right, stack.pop())
            stack.append(i)
        
        if right - left > 0:
            return right - left + 1
        else:
            return 0
print(Solution().findUnsortedSubarray( [2, 6, 4, 8, 10, 9, 15]))