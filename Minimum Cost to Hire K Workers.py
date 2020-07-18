'''

https://leetcode.com/explore/interview/card/google/59/array-and-strings/3061/

'''
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        paid_quality = []
        paid_wages = []
        res = 0.0

        N = len(quality)

        