class Solution:
    def firstUniqChar(self, s: 'str') -> 'int':
        dic = {}
        for c in s:
            if c in dic:
                dic[c] = dic[c] + 1
            else:
                dic[c] = 1
        for c,n in dic.items():
            if n == 1:
                return s.index(c)
        return -1

sol = Solution()
print(sol.firstUniqChar('abcdeabacd'))