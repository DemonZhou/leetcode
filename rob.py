class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)

        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0] , nums[1])

        dp = [ [ 0 ] for _ in range(N)] 

        dp[0] = nums[0]
        

        dp[1] = max(nums[0], nums[1])

        for i in range(2, N):
            dp[i] = max(dp[i - 1],dp[i - 2] + nums[i])
        
        print(dp)
        
        return dp[N - 1]

print(Solution().rob([2,1,1,2]))