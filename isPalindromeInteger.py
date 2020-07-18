class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        elif x == 0:
            return True
        else:
            reversed_num = 0
            while x > reversed_num:
                reversed_num = 10 * reversed_num + x % 10
                x = x // 10
            return x == reversed_num or x == reversed_num // 10

print(Solution().isPalindrome(121 ))