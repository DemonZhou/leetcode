class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []
        res = ""
        multi = 0

        for c in s:
            if c == '[':
                stack.append([multi,res])
                res = ""
                multi = 0
            elif  c >= '0' and c <= '9':
                multi = multi * 10 + int(c)
            elif c == ']':
                lastmulti, lastres = stack.pop()
                res = lastres + lastmulti * res
            else:
                res += c
            
        return res

        