'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

https://leetcode.com/explore/interview/card/google/59/array-and-strings/3050/
'''

class Solution(object):
    def reverse(self,nums,l,r):
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # find the max non-increasing suffix

        N = len(nums)
        high = N - 1
        while high - 1 >= 0 and nums[high] <= nums[high - 1]:
            high = high - 1
        
        if high == 0:
            nums.reverse()
            return

        pivot = high - 1
        successor = 0

        for i in range(N - 1,pivot,-1):
            if nums[i] > nums[pivot]:
                successor = i 
                break

        #swap
        nums[pivot] , nums[successor] = nums[successor], nums[pivot]
        self.reverse(nums,pivot+1,N-1)
