class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        nums1.sort()
        nums2.sort(reverse=True)
        for i in range(len(nums1)):
            res += nums1[i]*nums2[i]
        return res