class Solution(object):
    
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = 0
        pre = 0
        dic = {}

        dic[0] = 1 

        n = len(nums)

        for i in range(n):
            pre += nums[i]
            if (pre - k) in dic:
                count += dic[pre-k]
            if pre in dic:
                dic[pre] += 1
            else:
                dic[pre] = 1
        
        return count