class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""

        for  c in s:
            if c == " ":
                res += "%20"
            else:
                res += c
        return res