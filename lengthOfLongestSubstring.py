class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s : return 0
        res = 0
        cur = 0
        lookup = set()
        left = 0
        for i in range(len(s)):
            cur += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur -= 1
            res = max(cur,res)
            lookup.add(s[i])
        return res
Sol = Solution()
print(Sol.lengthOfLongestSubstring("bbbbb"))