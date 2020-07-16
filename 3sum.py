class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = set()

        N = 3
        target = 0
        self.find_sum(nums, 0, N , target , [] , ans)
        return list(ans)

    def find_sum(self, nums, start , N ,target, path ,ans):
        if len(nums) < N or N < 2: return 
        if N == 2:
            t = set()
            for i in range(start,len(nums)):
                if target - nums[i] in t:
                    ans.add(tuple(path + [target -  nums[i], nums[i]]))
                else:
                    t.add(nums[i])
        else:
            for i in range(start, len(nums)):
                if target > N * nums[ -1] or target < N * nums[i]:
                    break

                if i > start and nums[i] == nums[i - 1]:
                    continue
                self.find_sum(nums, i + 1, N - 1, target - nums[i], path + [nums[i]], ans)