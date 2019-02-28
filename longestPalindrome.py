class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        max_len = 0
        l = len(s)
        matrix = [[ 0 for x in range(l)] for y in range(l)]
        for i in range(l):
            j = 0
            while j <=i :
                if j == i:
                    matrix[i][j] = True
                elif i == j + 1:
                    matrix[i][j] = s[i] == s[j]
                else :
                    matrix[i][j] = s[i] == s[j] and matrix[i-1][j+1] == True
                if max_len < i - j and matrix[i][j] == True:
                    max_len = i - j
                    start = j
                    end = i
                j = j + 1
        return s[start:end + 1]

Sol = Solution()
print(Sol.longestPalindrome("babad"))
                
