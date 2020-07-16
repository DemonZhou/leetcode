class Solution(object):
    def __init__(self):
        self.ans = False
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        if not word:
            return True

        M = len(board)
        N = len(board[0])
        L = len(word)

        def backtrace(x, y,index):
            if self.ans:
                return
                
            if index >= L:
                return 
            if x < 0 or y < 0:
                return
            if x >= M or y >= N:
                return
            
            if visited[x][y]:
                return

            if board[x][y] != word[index]:
                return
            else:
                if index == L - 1:
                    self.ans = True
                    return
                else:
                    visited[x][y] = True
                    backtrace(x , y + 1 ,index + 1)
                    backtrace(x , y - 1 ,index + 1)
                    backtrace(x + 1, y ,index + 1)
                    backtrace(x - 1, y ,index + 1)
                    visited[x][y] = False
 
        visited = [ [False] * N for _ in range(M)]

        for i in range(M):
            for j in range(N):
                if board[i][j] == word[0]:
                    backtrace(i,j,0)
        return self.ans
