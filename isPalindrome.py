class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        if x == 0:
            return True
        
        if x < 10 :
            return True
        
        if x // 10 == x % 10:
            return True
        
        digits = len(str(x))
        n1 = int(list(str(x))[0])
        n2 = x % 10
        #print(n1)
        #print(n2)
        newx = (x - n2 - n1* 10 ** (digits - 1)) // 10
        #print(newx)
        return n1 == n2 and self.isPalindrome(newx)

print( Solution().isPalindrome(313) )