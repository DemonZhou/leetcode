class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if not s: return ""
        if n == 1: return s

        dp = [[False] * n for _ in range(n)]

        ans = ""

        for l in range(0,n):
            for j in range(n - l):
                if s[j] == s[j + l] and (j + 1 >= j + l - 1 or dp[j + 1][j + l - 1]):
                    dp[j][j + l] = True
                    ans = s[j : j + l + 1]
        return ans