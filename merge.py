class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        def sortBystart(e):
            return e[0]
        
        intervals.sort(sortBystart)

        res = []

        for interval in intervals:
            if len(res) == 0:
                res.append(interval)
                continue
            
            start = interval[0]
            end = interval[1]

            old_start = res[-1][0]
            old_end = res[-1][1]

            if start > old_end:
                res.append(interval)
            elif start <= old_end:
                res[-1][0] = old_start
                res[-1][1] = max(old_end,end)
        return res