class Solution(object):
    # https://leetcode-cn.com/problems/implement-strstr/
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        start = ite = 0

        M = len(haystack)
        N = len(needle)
        
        if N > M:
            return -1

        while start < M - N + 1:
            while start < M - N + 1 and haystack[start] != needle[0]:
                start += 1
            cur_len = 0
            ite = 0
            while ite < N and start < M and haystack[start] == needle[ite]:
                ite += 1 
                start += 1
                cur_len += 1

            if cur_len == N:
                return start - N
            start = start - cur_len + 1
            
        return -1
print(Solution().strStr("mississippi","issip"))