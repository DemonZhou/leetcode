class Solution:
    def twoSum(self, nums, target) :
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            if (target - num) in dic.keys():
                return [dic[target - num],i]
            dic[num] = i
        return None

Sol = Solution()
print(Sol.twoSum([2,7,11,15],9))