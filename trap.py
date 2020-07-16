class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        res = 0
        N = len(height)

        leftmost = [0] * N
        rightmost = [0] * N
        for i in range(N):
            if i == 0:
                leftmost[i] = max(0,height[i])
            if i > 0:
                leftmost[i] = max(leftmost[i - 1],height[i])
        for j in range(N - 1, - 1, -1):
            if j == N - 1:
                rightmost[j] = max(rightmost[j],height[j])
            if j < N - 1:
                rightmost[j] = max(height[j],rightmost[j + 1])
        
        for i in range(1,N - 1):
            if height[i] < leftmost[i] and height[i] < rightmost[i]:
                res += min(leftmost[i],rightmost[i]) - height[i]
        
        return res
    
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))