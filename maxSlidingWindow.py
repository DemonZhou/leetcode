class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []

        tmp = nums[0 : k ]

        res.append(max(tmp))

        for i in range(1, len(nums) - k + 1):
            reducenum = nums[ i - 1]
            addnum = nums[ i + k - 1]
            if reducenum < res[ - 1] :
                res.append(max(res[- 1] , addnum))
            elif reducenum == res[ - 1]:
                res.append( max(nums[i : i + k]) )
        return res