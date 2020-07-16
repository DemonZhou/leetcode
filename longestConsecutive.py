class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map = dict()

        res = 0

        for num in nums:
            if num not in hash_map:
                left = hash_map.get(num - 1, 0)
                right = hash_map.get(num + 1, 0)

                cur = left + right + 1
                res = max(res,cur)

                hash_map[num] = cur
                hash_map[num - left] = cur
                hash_map[num + right] = cur

        return res