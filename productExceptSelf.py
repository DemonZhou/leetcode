class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        output = []

        n = len(nums)
        prev = [1] * n
        next = [1] * n

        prev[0] = nums[0]
        for i in range(1,n):
            prev[i] = prev[i-1] * nums[i]
        
        next[n - 1] = nums[n - 1]

        for j in range(n - 2, -1 , -1):
            next[j] = next[j + 1] * nums[j]

        output.append(next[1])
        for i in range(1, n - 1):
            output.append( prev[i - 1] * next[i + 1] )

        output.append(prev[n - 2])

        return output