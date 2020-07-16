class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)

        left = [ 100000 for _ in range(n)]
        res = 0
        for i in range(n):
            if i >= 1:
                left[i] = min(prices[i],left[i - 1 ])
                res = max(res, prices[i] - left[i])
            else:
                left[i] = prices[i]      

Sol = Solution()
print(Sol.maxProfit([7,1,5,3,6,4]))