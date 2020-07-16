class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        S = sum(nums)
        N = len(nums)
        
        if S % 2 == 1:
            return False

        target = S / 2
        dp = [[False] * (target + 1) for _ in range(N)]
        for i in range(N):
            for j in range(201):
                if j == nums[i]:
                    dp[i][j] = True
                elif j > nums[i] :
                    dp[i][j] = dp[i][j] or dp[i - 1][j] or dp[i - 1][j - nums[i]] 
                else:
                    dp[i][j] = dp[i - 1][j]
        
        for r in dp:
            if r[target]:
                return True
        return False