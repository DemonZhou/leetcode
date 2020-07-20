class Solution(object):
    
    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        if shorter == longer:
            return [shorter * k]
        
        res = [0] * (k + 1)

        for i in range(k + 1):
            res[i] = (k - i) * shorter +  i * longer

        return res