'''

https://leetcode.com/explore/interview/card/google/59/array-and-strings/3058/

'''

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """

        
        N = len(seats)

        last = -1

        dis = 0

        for i in range(N):
            if seats[i]:
                dis = max(dis,i if last < 0 else (i - last)/2)
                last = i
        return max(dis,N - 1 - last)

print(Solution().maxDistToClosest([1,0,0,0,1,0,1]))