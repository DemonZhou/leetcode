class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        hashmap = [0] * 26
        ans = 0
        for t in tasks:
            hashmap[ord(t) - ord('A')] += 1

        hashmap.sort()
        while hashmap[25] > 0:
            i = 0
            while i <= n:
                if hashmap[25] == 0:
                    break
                if i < 26 and hashmap[25 - i] > 0:
                    hashmap[25 - i] -= 1
                ans += 1
                i += 1
            hashmap.sort()
        return ans
print(Solution().leastInterval(["A","A","A","B","B","B"] , 2))