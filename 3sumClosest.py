class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        if N < 3 :
            return

        nums.sort()
        ans = nums[0] + nums[1] + nums[2]


        for i in range(N):
            start = i + 1
            end = N - 1
            while start < end:
                summ = nums[i] + nums[start] + nums[end]
                if summ == target:
                    return target
                if abs(summ - target) < abs(ans - target):
                    ans = summ
                if summ < target:
                    start += 1
                if summ > target:
                    end -= 1
        return ans