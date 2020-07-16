class Solution(object):
    def __init__(self):
        self.res = 0
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        

        N = len(coins)

        coins.sort(reverse = True)

        def search(index, search_amount,count):

            if search_amount == 0:
                self.res = min(self.res, count)
                return
            
            if index > N - 1:
                return
            
            k = search_amount // coins[index]
            while k >= 0 and count + k < self.res:
                search(index + 1, search_amount - k * coins[index],count + k)
                k -= 1
        
        if amount == 0:
            return 0

        self.res = amount + 1

        search(0,amount,0)
        if self.res > amount:
            return -1
        else:
            return self.res

print(Solution().coinChange([2],3))