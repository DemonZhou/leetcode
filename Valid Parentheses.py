'''
https://leetcode.com/explore/interview/card/google/59/array-and-strings/467/
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict_s = {
            "]" : "[",
            "}" : "{",
            ")" : "("
        }

        stack = []

        for c in s:
            if c in dict_s.values():
                stack.append(c)
            elif c in dict_s.keys():
                stack.append(c)
                if len(stack) > 1 and stack[-2] == dict_s[c]:
                    stack.pop()
                    stack.pop()
        return len(stack) == 0
            