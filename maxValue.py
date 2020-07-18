class Solution(object):
    def __init__(self):
        self.ans = 0
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        M = len(grid)
        N = len(grid[0])
        dp = [[0] * N for _ in range(M)]
        dp[0][0] = grid[0][0]
        for i in range(1, N):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for i in range(1, M):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        
        for i in range(1, M):
            for j in range(1, N):
                dp[i][j] = grid[i][j] + max(dp[i - 1][j] , dp[i][j - 1])
            
        return dp[M - 1][N - 1]
    
print(Solution().maxValue(
  [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
))