class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        lenA = len(nums1)
        lenB = len(nums2)
        if (lenA + lenB) %2 == 1:
            return self.getKth(nums1,nums2, (lenA + lenB) // 2 )
        else:
            return  (self.getKth(nums1,nums2, (lenA + lenB) // 2 ) +  self.getKth(nums1,nums2, (lenA + lenB) // 2 - 1)) / 2.0

        
    def getKth(self,nums1,nums2,k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]

        mid1 , mid2 = len(nums1) // 2 , len(nums2) // 2
        midv1 , midv2 = nums1[mid1] , nums2[mid2]

        if mid1 + mid2 < k:
            if midv1 > midv2:
                return self.getKth(nums1,nums2[mid2 + 1:], k - mid2 - 1)
            else:
                return self.getKth(nums1[mid1 + 1:],nums2, k - mid1 -1)
        else:
            if midv1 > midv2:
                return self.getKth(nums1[:mid1],nums2, k)
            else:
                return self.getKth(nums1,nums2[:mid2],k)
