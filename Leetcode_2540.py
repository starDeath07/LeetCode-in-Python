class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        left, right = 0, 0

        while left < len(nums1) and right < len(nums2):
            if nums1[left] == nums2[right]:
                return nums1[left]

            if nums1[left] > nums2[right]:
                right += 1
            else:
                left += 1

        return -1
