class Solution(object):
    def __init__(self):
        self.summ = 0
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        
        N = len(nums)

        dp = [[0] * 2001 for _ in range(N)]
        dp[0][1000 + nums[0]] = 1
        dp[0][1000 - nums[0]] = 1

        for i in range(1,N):
            for s in range(-1000,1001):
                if dp[i - 1][s] > 0:
                    dp[i][s + nums[i] + 1000] += dp[i - 1][s + 1000]
                    dp[i][s - nums[i] + 1000] += dp[i - 1][s + 1000]
        return dp[N - 1][S + 1000]