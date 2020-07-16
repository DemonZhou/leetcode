<<<<<<< HEAD
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        def dfs(x,y):
            if not 0 <= x < len(grid) or not 0 <= y < len(grid[0]) or grid[x][y] != '1':
                return
            grid[x][y] = '2'
            dfs(x + 1,y)
            dfs(x - 1,y)
            dfs(x , y + 1)
            dfs(x, y - 1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    res += 1
        return res
=======
class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.DFS(grid,i,j)
                    res += 1
        return res
        


    def DFS(self,grid,i,j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '*'
        self.DFS(grid,i - 1,j)
        self.DFS(grid,i + 1,j)
        self.DFS(grid,i,j + 1)
        self.DFS(grid,i,j - 1)
>>>>>>> 4c9a2d276b1ddf2472647468ab660e7d695451cc
