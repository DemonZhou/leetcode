class Solution:
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        enum = 1
        res = []
        for i in range(len(nums)) :
            res.append(enum)
            enum *= nums[i]
        enum = 1
        for i in range(len(nums)-1,-1,-1) :
            res[i] *= enum
            enum *= nums[i]
        return res