class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        

        def getKthElement(k):
            offset1 = 0
            offset2 = 0

            while True:
                if offset1 == m:
                    return nums2[offset2 + k - 1]
                if offset2 == n:
                    return nums1[offset1 + k - 1]
                if k == 1:
                    return min(nums1[offset1] , nums2[offset2])
            
                newoffset1 = min(offset1 + k // 2 - 1 , m - 1)
            
                newoffset2 = min(offset2 + k // 2 - 1, n - 1)

                if nums1[newoffset1] <= nums2[newoffset2]:
                    k -= newoffset1 - offset1 + 1
                    offset1 = newoffset1 + 1
                    
                else:
                    k -= newoffset2 - offset2 + 1
                    offset2 = newoffset2 + 1

        m = len(nums1)
        n = len(nums2)

        if (m + n) % 2 == 1:
            return getKthElement( (m + n + 1) // 2 )
        else:
            return (getKthElement( (m + n) // 2 + 1) + getKthElement( (m + n) // 2)) / 2.0

Sol = Solution()
print(Sol.findMedianSortedArrays([1, 3],[2]))