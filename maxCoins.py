class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)

        dp = [[0] * (N + 2) for _ in range(N + 2)]
        val = [1] + nums + [1]

        for i in range(N - 1, - 1, -1):
            for j in range(i + 2, N + 2):
                for k in range(i + 1, j):
                    t = val[i] * val[k] * val[j]
                    t += dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], t)
        return dp[0][N + 1]