class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True

        N = len(nums)
        
        if N == 1:
            return True

        rightmost = 0

        for i in range(N):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= N - 1:
                    return True
        return False

print( Solution().canJump([2,3,1,1,4] ))