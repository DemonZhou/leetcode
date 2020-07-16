class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """

        if not T:
            return None

        N = len(T)
        res = [0] * N
        stack = []
        for i in range(N):
            if len(stack) == 0:
                stack.append(i)
            else:
                while len(stack) > 0 and T[stack[-1]] < T[i]:
                    previoysIndex = stack.pop()
                    res[previoysIndex] = i - previoysIndex
                stack.append(i)
        return res

