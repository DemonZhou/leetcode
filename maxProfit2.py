class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        dp = [[0] * 3 for _ in range(len(prices))]

        dp[0][0] = - prices[0]
        dp[0][1] = 0
        dp[0][2] = 0

        n = len(prices)

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0] , dp[i - 1][2] - prices[i])
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
        
        return max(dp[n - 1][1], dp[n - 1][2])