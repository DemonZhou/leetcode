class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix:
            return False

        M = len(matrix)
        N = len(matrix[0])
        
        x = M - 1
        y = 0

        while x >= 0 and y < N:
            if target == matrix[x][y]:
                return True
            elif target < matrix[x][y]:
                x -= 1
            elif target > matrix[x][y]:
                y += 1
        return False
