class Solution(object):
    def __init__(self):
        self.ans = 100000
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid:
            return 0

        M = len(grid)

        N = len(grid[0])


        dp = [ [0] * N for _ in range(M)]
        
        dp[-1][-1] = grid[-1][-1]

        for i in range(M - 1, -1 , -1):
            for j in range(N - 1, -1, -1):
                if i == M - 1 and j != N - 1:
                    dp[i][j] = grid[i][j] + dp[i][j + 1]
                elif j == N - 1 and i != M - 1:
                    dp[i][j] = grid[i][j] + dp[i + 1][j]
                elif i == M - 1 and j == N - 1:
                    continue
                else:
                    dp[i][j] = grid[i][j] + min(dp[i][j + 1],dp[i + 1][j])
            
        return dp[0][0]
    
print(Solution().minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))