class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        if len(nums)%2 == 0 :
            # even
            pos = len(nums)/2
            return (nums[pos] + nums[pos-1]) / 2.0
        else:
            # odd
            pos = math.floor(len(nums)/2)
            return nums[int(pos)]
