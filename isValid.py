class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif c in mapping.keys():
                top_elem = stack.pop() if stack else '#'
                if mapping[c] != top_elem:
                    return False
                
        return len(stack) == 0