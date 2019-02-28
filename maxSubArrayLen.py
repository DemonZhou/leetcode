class Solution:
    def maxSubArrayLen (self, nums: 'List[int]', k: 'int') -> 'int':
        dic = {0:-1}
        sum = 0
        max_len = 0
        for i in range(len(nums)):
            sum = sum + nums[i]
            dif = sum - k
            if dif in dic:
                max_len = max(max_len,i - dic[dif])
            if sum not in dic:
                dic[sum] = i
        return max_len            
    
Sol = Solution()
print(Sol.maxSubArrayLen([1,-1,5,-2,3],3))