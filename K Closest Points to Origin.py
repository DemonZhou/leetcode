'''

https://leetcode.com/explore/interview/card/google/59/array-and-strings/3062/

'''

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        return heapq.nsmallest(K, points, lambda (x, y): x * x + y * y)