class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        cache = {}
        for i in range(len(nums)):
            if nums[i] in cache:
                return [cache[nums[i]],i]
            cache[target - nums[i]] = i
sol = Solution()
print(sol.twoSum([2,7,3,4],5))