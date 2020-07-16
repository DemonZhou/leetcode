import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squareNums = [ i ** 2 for i in range(1, int(math.sqrt(n)) + 1)]

        dp = [float('inf')] * (n + 1)

        dp[0] = 0

        for i in range(1, n + 1):
            for sq in squareNums:
                if i < sq:
                    break
                dp[i] = min(dp[i], 1 + dp[i - sq])
        return int(dp[-1])
